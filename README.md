The Citadel Project

The Citadel is a personal Linux, cybersecurity, systems administration, and infrastructure portfolio lab built by Blake Swartz.

The project is designed to demonstrate practical hands-on experience with Linux administration, web hosting, SSH hardening, firewall management, Cloudflare Tunnel, Git/GitHub workflows, Docker deployment concepts, local monitoring, and security operations foundations.

The Citadel is both a live public portfolio site and a private learning lab.

⸻

Current Public Architecture

The current live architecture is:

Visitor
↓
Cloudflare Tunnel
↓
Apache on port 80
↓
/home/blakes52897/citadel-linux-lab/docker-site
↓
The Citadel website

Apache is the current active public frontend.

Docker was previously used to serve an NGINX-based version of the site on port 8080. That work is now documented as the Docker Deployment Lab, but Docker is not currently the active public frontend.

⸻

Live Site

The Citadel is publicly accessible through Cloudflare Tunnel.

Current public site:

rootandrook.com

⸻

Project Naming

The Citadel = main platform
Odysseus = AI operations assistant / AI workspace concept
Odysseus Memory Core = local RAG prototype
Argus = monitoring and visibility module
Sentinel = future detection and alerting module

⸻

Current Modules

The Citadel Website

The live website includes:

* Custom dark Citadel branding
* Homepage operations dashboard
* Project cards
* Dedicated project pages
* Live status.json telemetry
* Responsive layout
* Cloudflare-backed public access

⸻

Operations Dashboard / Argus Foundation

The homepage includes an operations dashboard powered by:

scripts/generate-status.sh
↓
docker-site/status.json
↓
browser-side JavaScript
↓
dashboard cards

Current telemetry includes:

* Last updated timestamp
* System uptime
* CPU load
* Memory usage
* Disk usage
* Apache status
* Cloudflare Tunnel status
* Fail2Ban status
* Tailscale status
* Docker status
* Running Docker container count
* Failed SSH attempts today
* Current Fail2Ban banned count
* Failed systemd units
* Latest Git commit

Argus is the planned monitoring and visibility module that will expand this dashboard into a more complete system health and security visibility layer.

⸻

Linux Hardening Lab

Documents the Linux security foundation for The Citadel.

Current security controls include:

* OpenSSH server
* SSH key-based remote administration
* UFW firewall
* Default deny incoming firewall posture
* Fail2Ban protection for SSH
* Authentication log review
* Tailscale remote administration
* Cloudflare Tunnel public routing

⸻

Docker Deployment Lab

Docker was used to prototype a containerized version of The Citadel site.

This lab documents:

* Dockerfile creation
* NGINX container deployment
* Port mapping
* Container lifecycle management
* Build-time vs runtime file behavior
* Transition from Docker public frontend to Apache public frontend

Docker remains part of the lab and learning environment, but Apache currently serves the live public site.

⸻

Cloudflare Tunnel

Cloudflare Tunnel provides public access to The Citadel without traditional router port forwarding.

Current state:

* Tunnel name: citadel-tunnel
* Cloudflared installed through APT
* Cloudflared runs as a system service
* Cloudflared is enabled at boot
* Public traffic routes through Cloudflare to Apache

⸻

Auth Monitor

Auth Monitor is the foundation for future security visibility.

Current sources and controls:

* /var/log/auth.log
* journald
* SSH authentication events
* Fail2Ban activity
* Failed login visibility
* Banned IP visibility

Auth Monitor will eventually feed into Sentinel.

⸻

SIEM Sandbox

SIEM Sandbox is a planned project area for log ingestion, detection logic, event review, and analyst workflow practice.

This may eventually integrate with:

* Wazuh
* Syslog pipelines
* Auth logs
* Apache logs
* Fail2Ban events
* Sentinel detection rules

⸻

Auto Deploy Pipeline

The Citadel uses Git and GitHub for source control and deployment tracking.

Current deployment workflow includes:

* Editing local site files
* Generating status telemetry
* Testing locally
* Committing changes to Git
* Pushing to GitHub
* Apache serving the updated project files

⸻

Odysseus and Self-Hosted AI Status

Odysseus is the planned AI operations assistant for The Citadel.

Self-hosted AI feasibility testing has been completed.

Tested components:

* Ollama
* llama3.2:3b
* llama3.1:8b
* qwen3:8b
* nomic-embed-text
* ChromaDB
* Local RAG
* Open WebUI
* Odysseus UI
* Terminal-based Odysseus Memory Core prototype

The local RAG prototype successfully ingested Citadel notes and project pages, retrieved relevant project context, and answered Citadel-specific questions.

However, CPU-only inference through the current Ubuntu VM is too slow for self-hosted AI to replace paid AI tools right now.

Current decision:

Self-hosted AI expansion is paused as an active priority.
The Citadel will continue focusing on Linux, cybersecurity, monitoring, detection, documentation, and portfolio development.
Self-hosted AI will be revisited later with stronger hardware.

Long-term AI goal:

Dedicated AI hardware node
NVIDIA GPU
More VRAM
Private Odysseus assistant
Persistent memory
Local knowledge base
Reduced reliance on external AI subscriptions

⸻

Current Hardware

Host machine:

* AMD Ryzen 7 5825U
* 8 cores / 16 threads
* 32 GB DDR4 RAM
* 1 TB NVMe SSD
* AMD Radeon integrated graphics
* No NVIDIA GPU

Current Ubuntu VM:

* 16 GB RAM allocated
* 6 vCPU allocated
* Approximately 48 GB root disk
* Disk usage currently high and should be monitored

Current hardware is sufficient for Linux, Docker, Apache, Cloudflare Tunnel, monitoring, RAG prototypes, and lightweight local AI experiments.

It is not ideal for smooth self-hosted AI assistant performance.

⸻

Repository Structure

citadel-linux-lab/
├── docker-site/
│   ├── index.html
│   ├── status.json
│   └── projects/
├── docs/
│   └── screenshots/
├── notes/
│   ├── citadel-notes.md
│   ├── citadel-current-state.md
│   └── odysseus-briefing.md
├── rag/
│   ├── ingest.py
│   └── query.py
├── scripts/
│   └── generate-status.sh
├── odysseus
└── README.md

⸻

Local Generated Files

The following local/generated files are intentionally ignored by Git:

rag/venv/
rag/vector-db/
rag/__pycache__/
__pycache__/
*.pyc

These can be rebuilt locally and should not be committed.

⸻

Current Priorities

Active priorities:

1. Continue building Argus as the monitoring and visibility module.
2. Improve the operations dashboard with useful live telemetry.
3. Add focused interactive telemetry to project pages.
4. Build Sentinel as the future security detection and alerting module.
5. Organize screenshots and evidence for portfolio documentation.
6. Add architecture diagrams.
7. Continue improving project pages and README documentation.
8. Keep self-hosted AI paused until future hardware upgrades.

⸻

Completed Milestones

Completed so far:

* Ubuntu VM created
* SSH configured
* UFW firewall enabled
* Apache installed and serving the live site
* Cloudflare Tunnel configured
* Git and GitHub workflow established
* Docker deployment lab created
* Dockerized NGINX website prototype built
* Public site routed through Cloudflare
* Custom Citadel landing page created
* Operations dashboard created
* status.json telemetry added
* Fail2Ban installed and configured
* Tailscale remote access configured
* Project pages created
* Odysseus Memory Core local RAG prototype built
* Open WebUI tested privately
* Odysseus UI connected to local Ollama
* Self-hosted AI feasibility assessed and paused

⸻

Next Major Build

The next major build phase is Argus.

Argus will become the all-seeing monitoring and visibility layer for The Citadel.

Initial Argus goals:

* Service health checks
* System health checks
* Docker/container visibility
* Fail2Ban visibility
* SSH authentication signal tracking
* Status dashboard improvements
* Project-page telemetry blocks

Future Sentinel work will build on Argus by adding security detection and alerting.
