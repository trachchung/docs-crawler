<!-- Source: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management -->

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#__docusaurus_skipToContent_fallback)
On this page
Manage Docker containers, images, volumes, networks, and Compose stacks — lifecycle ops, debugging, cleanup, and Dockerfile optimization.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#skill-metadata "Direct link to Skill metadata")  
| Source  | Optional — install with `hermes skills install official/devops/docker-management`  |  
| --- | --- |  
| Path  | `optional-skills/devops/docker-management`  |  
| Version  | `1.0.0`  |  
| Author  | sprmn24  |  
| License  | MIT  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `docker`, `containers`, `devops`, `infrastructure`, `compose`, `images`, `volumes`, `networks`, `debugging`  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#reference-full-skillmd "Direct link to Reference: full SKILL.md")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# Docker Management
Manage Docker containers, images, volumes, networks, and Compose stacks using standard Docker CLI commands. No additional dependencies beyond Docker itself.
## When to Use[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#when-to-use "Direct link to When to Use")
  * Run, stop, restart, remove, or inspect containers
  * Build, pull, push, tag, or clean up Docker images
  * Work with Docker Compose (multi-service stacks)
  * Manage volumes or networks
  * Debug a crashing container or analyze logs
  * Check Docker disk usage or free up space
  * Review or optimize a Dockerfile


## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#prerequisites "Direct link to Prerequisites")
  * Docker Engine installed and running
  * User added to the `docker` group (or use `sudo`)
  * Docker Compose v2 (included with modern Docker installations)


Quick check:

```
docker--version&&docker compose version
```

## Quick Reference[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#quick-reference "Direct link to Quick Reference")  
| Task  | Command  |  
| --- | --- |  
| Run container (background)  | `docker run -d --name NAME IMAGE`  |  
| Stop + remove  | `docker stop NAME && docker rm NAME`  |  
| View logs (follow)  | `docker logs --tail 50 -f NAME`  |  
| Shell into container  | `docker exec -it NAME /bin/sh`  |  
| List all containers  | `docker ps -a`  |  
| Build image  | `docker build -t TAG .`  |  
| Compose up  | `docker compose up -d`  |  
| Compose down  | `docker compose down`  |  
| Disk usage  | `docker system df`  |  
| Cleanup dangling  | `docker image prune && docker container prune`  |  
## Procedure[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#procedure "Direct link to Procedure")
### 1. Identify the domain[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#1-identify-the-domain "Direct link to 1. Identify the domain")
Figure out which area the request falls into:
  * **Container lifecycle** → run, stop, start, restart, rm, pause/unpause
  * **Container interaction** → exec, cp, logs, inspect, stats
  * **Image management** → build, pull, push, tag, rmi, save/load
  * **Docker Compose** → up, down, ps, logs, exec, build, config
  * **Volumes & networks** → create, inspect, rm, prune, connect
  * **Troubleshooting** → log analysis, exit codes, resource issues


### 2. Container operations[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#2-container-operations "Direct link to 2. Container operations")
**Run a new container:**

```
# Detached service with port mappingdocker run -d--name web -p8080:80 nginx# With environment variablesdocker run -d-ePOSTGRES_PASSWORD=secret -ePOSTGRES_DB=mydb --name db postgres:16# With persistent data (named volume)docker run -d-v pgdata:/var/lib/postgresql/data --name db postgres:16# For development (bind mount source code)docker run -d-v$(pwd)/src:/app/src -p3000:3000 --name dev my-app# Interactive debugging (auto-remove on exit)docker run -it--rm ubuntu:22.04 /bin/bash# With resource limits and restart policydocker run -d--memory=512m --cpus=1.5--restart=unless-stopped --name app my-app
```

Key flags: `-d` detached, `-it` interactive+tty, `--rm` auto-remove, `-p` port (host:container), `-e` env var, `-v` volume, `--name` name, `--restart` restart policy.
**Manage running containers:**

```
dockerps# running containersdockerps-a# all (including stopped)docker stop NAME                 # graceful stopdocker start NAME                # start stopped containerdocker restart NAME              # stop + startdockerrm NAME                   # remove stopped containerdockerrm-f NAME                # force remove running containerdocker container prune           # remove ALL stopped containers
```

**Interact with containers:**

```
dockerexec-it NAME /bin/sh          # shell access (use /bin/bash if available)dockerexec NAME env# view environment variablesdockerexec-u root NAME apt update    # run as specific userdocker logs --tail100-f NAME         # follow last 100 linesdocker logs --since 2h NAME            # logs from last 2 hoursdockercp NAME:/path/file ./local      # copy file from containerdockercp ./file NAME:/path/           # copy file to containerdocker inspect NAME                    # full container details (JSON)docker stats --no-stream               # resource usage snapshotdockertop NAME                        # running processes
```

### 3. Image management[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#3-image-management "Direct link to 3. Image management")

```
# Builddocker build -t my-app:latest .docker build -t my-app:prod -f Dockerfile.prod .docker build --no-cache -t my-app .# clean rebuildDOCKER_BUILDKIT=1docker build -t my-app .# faster with BuildKit# Pull and pushdocker pull node:20-alpinedocker login ghcr.iodocker tag my-app:latest registry/my-app:v1.0docker push registry/my-app:v1.0# Inspectdocker images                          # list local imagesdockerhistory IMAGE                   # see layersdocker inspect IMAGE                   # full details# Cleanupdocker image prune                     # remove dangling (untagged) imagesdocker image prune -a# remove ALL unused images (careful!)docker image prune -a--filter"until=168h"# unused images older than 7 days
```

### 4. Docker Compose[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#4-docker-compose "Direct link to 4. Docker Compose")

```
# Start/stopdocker compose up -d# start all services detacheddocker compose up -d--build# rebuild images before startingdocker compose down                    # stop and remove containersdocker compose down -v# also remove volumes (DESTROYS DATA)# Monitoringdocker compose ps# list servicesdocker compose logs -f api             # follow logs for specific servicedocker compose logs --tail50# last 50 lines all services# Interactiondocker compose exec api /bin/sh        # shell into running servicedocker compose run --rm api npmtest# one-off command (new container)docker compose restart api             # restart specific service# Validationdocker compose config                  # validate and view resolved config
```

**Minimal compose.yml example:**

```
services:api:build: .ports:-"3000:3000"environment:- DATABASE_URL=postgres://user:pass@db:5432/mydbdepends_on:db:condition: service_healthydb:image: postgres:16-alpineenvironment:POSTGRES_USER: userPOSTGRES_PASSWORD: passPOSTGRES_DB: mydbvolumes:- pgdata:/var/lib/postgresql/datahealthcheck:test:["CMD-SHELL","pg_isready -U user"]interval: 10stimeout: 5sretries:5volumes:  pgdata:
```

### 5. Volumes and networks[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#5-volumes-and-networks "Direct link to 5. Volumes and networks")

```
# Volumesdocker volume ls# list volumesdocker volume create mydata            # create named volumedocker volume inspect mydata           # details (mount point, etc.)docker volume rm mydata                # remove (fails if in use)docker volume prune                    # remove unused volumes# Networksdocker network ls# list networksdocker network create mynet            # create bridge networkdocker network inspect mynet           # details (connected containers)docker network connect mynet NAME      # attach container to networkdocker network disconnect mynet NAME   # detach containerdocker network rm mynet                # remove networkdocker network prune                   # remove unused networks
```

### 6. Disk usage and cleanup[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#6-disk-usage-and-cleanup "Direct link to 6. Disk usage and cleanup")
Always start with a diagnostic before cleaning:

```
# Check what's using spacedocker system df# summarydocker system df-v# detailed breakdown# Targeted cleanup (safe)docker container prune                 # stopped containersdocker image prune                     # dangling imagesdocker volume prune                    # unused volumesdocker network prune                   # unused networks# Aggressive cleanup (confirm with user first!)docker system prune                    # containers + images + networksdocker system prune -a# also unused imagesdocker system prune -a--volumes# EVERYTHING — named volumes too
```

**Warning:** Never run `docker system prune -a --volumes` without confirming with the user. This removes named volumes with potentially important data.
## Pitfalls[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#pitfalls "Direct link to Pitfalls")  
| Problem  | Cause  | Fix  |  
| --- | --- | --- |  
| Container exits immediately  | Main process finished or crashed  | Check `docker logs NAME`, try `docker run -it --entrypoint /bin/sh IMAGE`  |  
| "port is already allocated"  | Another process using that port  |  `docker ps` or `lsof -i :PORT` to find it  |  
| "no space left on device"  | Docker disk full  |  `docker system df` then targeted prune  |  
| Can't connect to container  | App binds to 127.0.0.1 inside container  | App must bind to `0.0.0.0`, check `-p` mapping  |  
| Permission denied on volume  | UID/GID mismatch host vs container  | Use `--user $(id -u):$(id -g)` or fix permissions  |  
| Compose services can't reach each other  | Wrong network or service name  | Services use service name as hostname, check `docker compose config`  |  
| Build cache not working  | Layer order wrong in Dockerfile  | Put rarely-changing layers first (deps before source code)  |  
| Image too large  | No multi-stage build, no .dockerignore  | Use multi-stage builds, add `.dockerignore`  |  
## Verification[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#verification "Direct link to Verification")
After any Docker operation, verify the result:
  * **Container started?** → `docker ps` (check status is "Up")
  * **Logs clean?** → `docker logs --tail 20 NAME` (no errors)
  * **Port accessible?** → `curl -s http://localhost:PORT` or `docker port NAME`
  * **Image built?** → `docker images | grep TAG`
  * **Compose stack healthy?** → `docker compose ps` (all services "running" or "healthy")
  * **Disk freed?** → `docker system df` (compare before/after)


## Dockerfile Optimization Tips[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#dockerfile-optimization-tips "Direct link to Dockerfile Optimization Tips")
When reviewing or creating a Dockerfile, suggest these improvements:
  1. **Multi-stage builds** — separate build environment from runtime to reduce final image size
  2. **Layer ordering** — put dependencies before source code so changes don't invalidate cached layers
  3. **Combine RUN commands** — fewer layers, smaller image
  4. **Use .dockerignore** — exclude `node_modules`, `.git`, `__pycache__`, etc.
  5. **Pin base image versions** — `node:20-alpine` not `node:latest`
  6. **Run as non-root** — add `USER` instruction for security
  7. **Use slim/alpine bases** — `python:3.12-slim` not `python:3.12`


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#reference-full-skillmd)
  * [When to Use](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#when-to-use)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#prerequisites)
  * [Quick Reference](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#quick-reference)
  * [Procedure](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#procedure)
    * [1. Identify the domain](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#1-identify-the-domain)
    * [2. Container operations](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#2-container-operations)
    * [3. Image management](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#3-image-management)
    * [4. Docker Compose](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#4-docker-compose)
    * [5. Volumes and networks](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#5-volumes-and-networks)
    * [6. Disk usage and cleanup](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#6-disk-usage-and-cleanup)
  * [Verification](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#verification)
  * [Dockerfile Optimization Tips](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management#dockerfile-optimization-tips)


