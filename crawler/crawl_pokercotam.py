#!/usr/bin/env python3
"""Crawl poker tournament data from https://pokercotam.net/

pokercotam.net is a Firebase/Firestore-backed single-page app. Instead of
scraping the JavaScript-rendered DOM (fragile, Tailwind-only class names, only
shows the currently-selected day), this script reads the underlying Firestore
collections directly through the public REST `:runQuery` endpoint - the exact
same data the web app subscribes to. This yields complete, structured data.

The Firebase config (project / database / web API key) was extracted from the
site's JS bundle. The API key is a *public* client key embedded in the page;
Firestore security rules permit anonymous reads of these collections via query.

No external dependencies - uses only the Python standard library.

Usage:
    python crawl_pokercotam.py                 # crawl everything to ./output
    python crawl_pokercotam.py -o ./data       # custom output dir
    python crawl_pokercotam.py --collections tournaments clubs
"""

import argparse
import csv
import json
import os
import time
import urllib.error
import urllib.request

# --- Firebase / Firestore configuration (public client values from the JS bundle) ---
PROJECT_ID = "gen-lang-client-0830763378"
DATABASE_ID = "ai-studio-8015b34f-a42a-44f7-96c7-bb1e434be23f"
API_KEY = "AIzaSyD_BHe-WDRK8IhZVnFpx69VvS0kkKvRZTU"
GMP_ID = "1:160858841310:web:dfa81d00f9345ff994a24f"

BASE_URL = (
    f"https://firestore.googleapis.com/v1/projects/{PROJECT_ID}"
    f"/databases/{DATABASE_ID}/documents"
)

# Collections the SPA subscribes to (seen in the Firestore Listen channel).
DEFAULT_COLLECTIONS = ["tournaments", "clubs", "news", "banners"]
# Single documents (not collections) the app also reads.
SINGLE_DOCS = ["system/siteSettings"]

HEADERS = {
    "Content-Type": "application/json",
    "X-Firebase-GMPID": GMP_ID,
    "X-Goog-Api-Client": "gl-js/ fire/12.12.0",
}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Crawl poker tournament data from pokercotam.net (Firestore REST)"
    )
    parser.add_argument(
        "--output", "-o", default="./output", help="Output directory (default: ./output)"
    )
    parser.add_argument(
        "--collections",
        nargs="+",
        default=DEFAULT_COLLECTIONS,
        help=f"Collections to crawl (default: {' '.join(DEFAULT_COLLECTIONS)})",
    )
    parser.add_argument(
        "--page-size", type=int, default=300, help="Documents per query page (default: 300)"
    )
    parser.add_argument(
        "--no-csv", action="store_true", help="Skip writing tournaments.csv"
    )
    parser.add_argument(
        "--delay", type=float, default=0.3, help="Delay between requests in seconds (default: 0.3)"
    )
    return parser.parse_args()


# --- Firestore value decoding -------------------------------------------------

def decode_value(value: dict):
    """Convert a single Firestore typed Value into a native Python value."""
    if "stringValue" in value:
        return value["stringValue"]
    if "integerValue" in value:
        return int(value["integerValue"])
    if "doubleValue" in value:
        return float(value["doubleValue"])
    if "booleanValue" in value:
        return value["booleanValue"]
    if "timestampValue" in value:
        return value["timestampValue"]
    if "nullValue" in value:
        return None
    if "referenceValue" in value:
        return value["referenceValue"]
    if "geoPointValue" in value:
        return value["geoPointValue"]
    if "bytesValue" in value:
        return value["bytesValue"]
    if "arrayValue" in value:
        return [decode_value(v) for v in value["arrayValue"].get("values", [])]
    if "mapValue" in value:
        return decode_fields(value["mapValue"].get("fields", {}))
    # Unknown type: return the raw wrapper so no data is silently lost.
    return value


def decode_fields(fields: dict) -> dict:
    return {key: decode_value(val) for key, val in fields.items()}


def decode_document(doc: dict) -> dict:
    """Flatten a Firestore document into {id, ...fields, _createTime, _updateTime}."""
    decoded = decode_fields(doc.get("fields", {}))
    decoded["id"] = doc["name"].rsplit("/", 1)[-1]
    decoded["_createTime"] = doc.get("createTime")
    decoded["_updateTime"] = doc.get("updateTime")
    return decoded


# --- HTTP helpers -------------------------------------------------------------

def post_json(url: str, body: dict) -> list | dict:
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=HEADERS, method="POST")
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def get_json(url: str) -> dict:
    req = urllib.request.Request(url, headers=HEADERS, method="GET")
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


# --- Crawling -----------------------------------------------------------------

def crawl_collection(collection: str, page_size: int, delay: float) -> list[dict]:
    """Fetch every document in a collection via paginated `:runQuery`.

    Paginates by ordering on the document name (__name__) and using a startAt
    cursor, so it works regardless of collection size.
    """
    url = f"{BASE_URL}:runQuery?key={API_KEY}"
    docs: list[dict] = []
    last_name: str | None = None

    while True:
        structured_query = {
            "from": [{"collectionId": collection}],
            "orderBy": [{"field": {"fieldPath": "__name__"}, "direction": "ASCENDING"}],
            "limit": page_size,
        }
        if last_name:
            structured_query["startAt"] = {
                "values": [{"referenceValue": last_name}],
                "before": False,
            }

        result = post_json(url, {"structuredQuery": structured_query})
        page = [row["document"] for row in result if "document" in row]
        if not page:
            break

        docs.extend(page)
        if len(page) < page_size:
            break
        last_name = page[-1]["name"]
        time.sleep(delay)

    return [decode_document(d) for d in docs]


def crawl_single_doc(path: str) -> dict | None:
    url = f"{BASE_URL}/{path}?key={API_KEY}"
    try:
        doc = get_json(url)
    except urllib.error.HTTPError as exc:
        print(f"    x {path}  (HTTP {exc.code})")
        return None
    return decode_document(doc)


def save_json(filepath: str, data):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def save_csv(filepath: str, rows: list[dict]):
    if not rows:
        return
    # Union of keys across all rows, stable order: first row's keys, then any extras.
    columns: list[str] = []
    seen = set()
    for row in rows:
        for key in row:
            if key not in seen:
                seen.add(key)
                columns.append(key)

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in columns})


def main():
    args = parse_args()
    out_dir = os.path.join(args.output, "pokercotam")

    print(f"\n{'=' * 60}")
    print("  Crawling pokercotam.net (Firestore REST)")
    print(f"  Project: {PROJECT_ID}")
    print(f"  Output:  {out_dir}")
    print(f"{'=' * 60}")

    summary: dict[str, int] = {}

    for collection in args.collections:
        print(f"\n  Collection: {collection}")
        try:
            rows = crawl_collection(collection, args.page_size, args.delay)
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", "replace")[:200]
            print(f"    x failed (HTTP {exc.code}): {detail}")
            continue

        save_json(os.path.join(out_dir, f"{collection}.json"), rows)
        summary[collection] = len(rows)
        print(f"    + {len(rows)} document(s) -> {collection}.json")

        if collection == "tournaments" and not args.no_csv:
            save_csv(os.path.join(out_dir, "tournaments.csv"), rows)
            print("    + tournaments.csv")

        time.sleep(args.delay)

    for path in SINGLE_DOCS:
        doc = crawl_single_doc(path)
        if doc is not None:
            name = path.replace("/", "_")
            save_json(os.path.join(out_dir, f"{name}.json"), doc)
            print(f"\n  + {path} -> {name}.json")

    print(f"\n{'=' * 60}")
    print("  Done:")
    for collection, count in summary.items():
        print(f"    {collection:<14} {count} document(s)")
    print(f"{'=' * 60}\n")


if __name__ == "__main__":
    main()
