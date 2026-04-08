#!/usr/bin/env python3
"""General-purpose documentation site crawler. Saves each page as a separate markdown file."""

import argparse
import asyncio
import os
import re
from urllib.parse import urlparse

from crawl4ai import AsyncWebCrawler, BrowserConfig, CacheMode, CrawlerRunConfig
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

SKIP_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico", ".webp",
    ".pdf", ".zip", ".tar", ".gz",
    ".css", ".js", ".woff", ".woff2", ".ttf", ".eot",
    ".mp4", ".mp3", ".wav", ".avi",
}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Crawl documentation sites and save each page as markdown"
    )
    parser.add_argument("urls", nargs="+", help="Seed URL(s) to crawl")
    parser.add_argument(
        "--output", "-o", default="./output", help="Output directory (default: ./output)"
    )
    parser.add_argument(
        "--delay", "-d", type=float, default=1.0, help="Mean delay between requests in seconds (default: 1.0)"
    )
    parser.add_argument(
        "--max-concurrent", "-c", type=int, default=5, help="Max concurrent requests (default: 5)"
    )
    parser.add_argument(
        "--max-pages", "-m", type=int, default=1000, help="Max pages to crawl per site (default: 1000)"
    )
    parser.add_argument(
        "--wait", "-w", type=float, default=5.0,
        help="Seconds to wait for JS rendering before capturing (default: 5.0, set 0 for static sites)",
    )
    return parser.parse_args()


def get_domain(url: str) -> str:
    return urlparse(url).netloc


def normalize_url(url: str) -> str:
    """Strip fragments, query params, and trailing slashes."""
    parsed = urlparse(url)
    path = parsed.path
    if path != "/" and path.endswith("/"):
        path = path.rstrip("/")
    return f"{parsed.scheme}://{parsed.netloc}{path}"


def should_skip_url(url: str) -> bool:
    """Skip non-page URLs like images, scripts, mailto, etc."""
    if not url.startswith(("http://", "https://")):
        return True
    parsed = urlparse(url)
    ext = os.path.splitext(parsed.path)[1].lower()
    return ext in SKIP_EXTENSIONS


def url_to_filepath(url: str, output_dir: str) -> str:
    """Convert URL path to a local file path. Uses index.md inside directories
    to avoid file/directory collisions (e.g. /guide vs /guide/something)."""
    parsed = urlparse(url)
    domain = parsed.netloc
    path = parsed.path.strip("/")
    if not path:
        return os.path.join(output_dir, domain, "index.md")
    # Sanitize each segment for filesystem
    segments = [re.sub(r'[<>:"|?*\\]', "_", s) for s in path.split("/")]
    return os.path.join(output_dir, domain, *segments, "index.md")


def extract_same_domain_links(result, domain: str) -> set[str]:
    """Pull all same-domain links from a crawl result."""
    links: set[str] = set()
    for category in ("internal", "external"):
        for link_info in result.links.get(category, []):
            href = link_info.get("href", "")
            if not href or should_skip_url(href):
                continue
            normalized = normalize_url(href)
            if get_domain(normalized) == domain:
                links.add(normalized)
    return links


def get_markdown_text(result) -> str:
    """Extract filtered markdown from a CrawlResult, falling back to raw."""
    md = result.markdown
    if hasattr(md, "fit_markdown") and md.fit_markdown:
        return md.fit_markdown
    if hasattr(md, "raw_markdown"):
        return md.raw_markdown
    return str(md) if md else ""


def save_markdown(filepath: str, url: str, content: str):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"<!-- Source: {url} -->\n\n{content}")


async def crawl_site(
    seed_url: str,
    output_dir: str,
    delay: float,
    max_concurrent: int,
    max_pages: int,
    wait: float,
):
    domain = get_domain(seed_url)
    seed_normalized = normalize_url(seed_url)

    visited: set[str] = set()
    failed: set[str] = set()
    queue: set[str] = {seed_normalized}
    total_saved = 0

    print(f"\n{'=' * 60}")
    print(f"  Site:   {domain}")
    print(f"  Seed:   {seed_url}")
    print(f"  Output: {os.path.join(output_dir, domain)}")
    print(f"{'=' * 60}")

    browser_config = BrowserConfig(headless=True)
    md_generator = DefaultMarkdownGenerator(
        content_filter=PruningContentFilter(threshold=0.4, threshold_type="fixed")
    )
    crawler_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        markdown_generator=md_generator,
        page_timeout=60000,
        delay_before_return_html=wait,
        mean_delay=delay,
        semaphore_count=max_concurrent,
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        while queue and total_saved < max_pages:
            remaining = max_pages - total_saved
            batch = list(queue)[:remaining]
            queue -= set(batch)

            print(f"\n  Batch: {len(batch)} URL(s)  |  Saved so far: {total_saved}  |  Queued: {len(queue)}")

            if len(batch) == 1:
                results = [await crawler.arun(url=batch[0], config=crawler_config)]
            else:
                results = await crawler.arun_many(urls=batch, config=crawler_config)

            for result in results:
                if not result.success:
                    failed.add(result.url)
                    print(f"    x {result.url}  ({result.error_message})")
                    continue

                visited.add(result.url)
                markdown = get_markdown_text(result)
                if not markdown.strip():
                    print(f"    - {result.url}  (empty)")
                    continue

                filepath = url_to_filepath(result.url, output_dir)
                save_markdown(filepath, result.url, markdown)
                total_saved += 1
                print(f"    + {result.url}")

                new_links = extract_same_domain_links(result, domain)
                new_count = 0
                for link in new_links:
                    if link not in visited and link not in failed and link not in queue:
                        queue.add(link)
                        new_count += 1
                if new_count:
                    print(f"      -> discovered {new_count} new link(s)")

    print(f"\n  Done: {total_saved} pages saved from {domain}\n")
    return total_saved


async def main():
    args = parse_args()

    total = 0
    for url in args.urls:
        count = await crawl_site(
            url, args.output, args.delay, args.max_concurrent, args.max_pages, args.wait
        )
        total += count

    print(f"{'=' * 60}")
    print(f"  Total: {total} pages saved to {args.output}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    asyncio.run(main())
