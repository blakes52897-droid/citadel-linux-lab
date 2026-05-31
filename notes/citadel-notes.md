		# The Citadel - Ubuntu Security Lab

Started:
# 2026-05-23

---

# Objective

Build a Linux-based cybersecurity and infrastructure homelab for learning:

- Linux administration
- Networking
- Cybersecurity
- System hardening
- Web hosting
- System monitoring
- Command-line management

Project Name:
# THE CITADEL ♜

Tagline:
> Fortify The Position

---

# Environment

## Host System
- VirtualBox

## Guest Operating System
- Ubuntu Linux

## Web Server
- Apache2

## Security Services
- OpenSSH Server
- UFW Firewall

---

# Lab Architecture

```text
Host PC
└── VirtualBox
    └── Ubuntu VM
        └── Apache2 Web Server
            └── The Citadel Website
```

---

# 2026-05-23

# System Updates

Updated Ubuntu packages and repositories.

Commands used:

```bash
sudo apt update && sudo apt upgrade -y
```

Lessons Learned:
- Linux systems use package repositories
- apt handles package management
- Keeping systems updated is critical for security

---

# 2026-05-23

# SSH Setup

Installed and configured OpenSSH Server for remote administration.

Commands used:

```bash
sudo apt install openssh-server -y
sudo systemctl start ssh
sudo systemctl enable ssh
sudo systemctl status ssh
```

Lessons Learned:
- Linux services are managed with systemctl
- SSH allows secure remote administration
- Services can be enabled to start automatically on boot

---

# 2026-05-23

# Network Configuration

Checked network interfaces and local IP address.

Commands used:

```bash
ip a
```

Important Information:
- Local VM IP Address: 10.0.2.15
- Network Interface: enp0s3

Lessons Learned:
- VirtualBox NAT networking assigns private internal IP addresses
- Linux network interfaces can be inspected with ip commands

---

# 2026-05-23

# Apache Web Server

Installed Apache2 and configured website hosting.

Commands used:

```bash
sudo apt install apache2 -y
sudo systemctl start apache2
sudo systemctl enable apache2
sudo systemctl status apache2
```

Lessons Learned:
- Apache serves website files from:
```text
/var/www/html
```

- Main landing page file:
```text
index.html
```

- Apache runs as a background service (daemon)

---

# 2026-05-23

# Website Customization

Created custom cybersecurity-themed landing page called:

# THE CITADEL

Theme Direction:
- Luxury monochrome aesthetic
- Chess-inspired branding
- Tactical infrastructure feel
- Black and white UI
- Minimalist cybersecurity dashboard

Technologies Used:
- HTML
- CSS

Lessons Learned:
- HTML structures web pages
- CSS controls appearance and layout
- Websites can be hosted directly from Linux servers

---

# 2026-05-23

# Firewall Configuration

Installed and configured UFW firewall.

Commands used:

```bash
sudo apt install ufw -y
sudo ufw allow ssh
sudo ufw enable
sudo ufw status
```

Lessons Learned:
- UFW manages Linux firewall rules
- Only necessary ports should be exposed
- SSH traffic must be explicitly allowed

---

# Linux Commands Learned

## Navigation

```bash
pwd
ls
cd
```

## File Management

```bash
mkdir
mv
nano
```

## Service Management

```bash
systemctl status
systemctl start
systemctl enable
```

## Networking

```bash
ip a
```

## Package Management

```bash
apt install
apt update
apt upgrade
```

---

# Troubleshooting Notes

## 2026-05-23
### SSH Service Inactive

Issue:
SSH service initially showed:

```text
inactive (dead)
```

Fix:
Started the SSH service manually.

Command used:

```bash
sudo systemctl start ssh
```

Lesson Learned:
Linux services may be installed but not currently running.

---

## 2026-05-23
### Linux Filenames With Spaces

Issue:
Attempted to open a file named:

```text
Citadel Notes
```

Using:

```bash
cd Citadel Notes
```

Resulted in:

```text
too many arguments
```

Fix:
Renamed the file using hyphens instead of spaces.

Command used:

```bash
mv "Citadel Notes" citadel-notes.md
```

Lesson Learned:
Linux handles spaces in filenames differently than expected.
Hyphens and underscores are preferred.

---

# Security Concepts Learned

## SSH

SSH provides encrypted remote administration for Linux systems.

---

## Principle of Least Exposure

Only necessary ports and services should be enabled.

---

## Firewall Management

Firewalls help restrict unauthorized network access.

---

## Service Management

Services should:
- be monitored
- started intentionally
- enabled only when necessary

---

# Current Status

## Active Services

- Apache2
- SSH
- UFW Firewall

## Website Status

The Citadel webpage is currently hosted locally from the Ubuntu VM.

Access URL:

```text
http://10.0.2.15
```

---

# Future Improvements

## Security
- Install Fail2Ban
- Learn log analysis
- Configure HTTPS
- Harden SSH configuration

## Infrastructure
- Add live system statistics
- Create dashboards
- Learn Docker
- Explore reverse proxies

## Monitoring
- Study auth logs
- Learn journalctl
- Configure monitoring tools

## Portfolio
- Upload project to GitHub
- Add screenshots
- Create architecture diagrams
- Document future labs

---

# Reflection

This project provided hands-on experience with:

- Linux administration
- Web hosting
- Networking
- Firewall management
- System services
- Virtualization
- HTML/CSS customization
- Troubleshooting
- Command-line workflows

The Citadel serves as the foundation for future cybersecurity and infrastructure projects.

♜ Fortify The Position
# 2026-05-24

# Fail2Ban Intrusion Prevention

Completed:
- Installed Fail2Ban
- Enabled automatic startup
- Verified service status
- Began intrusion prevention monitoring

Commands Used:

```bash
sudo apt install fail2ban -y
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
sudo systemctl status fail2ban
sudo fail2ban-client status
sudo fail2ban-client status sshd
```

Lessons Learned:
- Fail2Ban monitors logs for suspicious authentication behavior
- Repeated failed login attempts can trigger automatic alerts
- Security services can run continuously in the background
- Defense-in-depth improves overall security posture

Security Concepts:
- Brute Force Mitigation
- Intrusion Prevention
- Log Monitoring
- Service Hardening

Observed:
- SSH jail monitoring
- Authentication telemetry
- Active security service management

Notes:
Fail2Ban adds an additional defensive layer to The Citadel by automatically responding to repeated failed authentication attempts.

---
---
# Authentication Failure Observation

Observed failed authentication attempts in:

```bash
/var/log/auth.log
```

Observed Events:
- failed su authentication
- PAM authentication failures
- user privilege escalation attempts

Example Log Indicators:
- authentication failure
- FAILED SU
- session opened
- session closed

Lessons Learned:
Linux systems generate detailed authentication telemetry which can be monitored for suspicious behavior and privilege escalation attempts.
# Lessons Learned

- Learned the difference between `su - username` and incorrect syntax like `su -Maks1012`
- Observed failed authentication attempts directly in `/var/log/auth.log`
- Learned how sudo sessions appear in Linux logs
- Discovered GitHub no longer accepts account passwords for Git pushes and requires Personal Access Tokens
- Learned that terminal commands are sensitive to spacing (`cd~` vs `cd ~`)
- Configured and verified Fail2Ban SSH jail protection
- Learned how Git tracks infrastructure/documentation changes with commits
- Successfully pushed homelab documentation to GitHub repository
- Learned how to verify Git synchronization with git status

---

# 2026-05-25 Notes

# Git + GitHub Integration

## Completed
- Installed and verified Git
- Configured global Git username and email
- Initialized local Git repository inside `~/citadel-linux-lab`
- Created initial commit
- Created private GitHub repository
- Connected local repository to GitHub remote
- Renamed default branch from `master` → `main`
- Successfully pushed project to GitHub
- Verified synchronization with:
  ```bash
  git status
  ```

## Commands Learned

### Configure Git Identity
```bash
git config --global user.name "Blake Swartz"
git config --global user.email "bswartz52897@gmail.com"
```

### Initialize Repository
```bash
git init
```

### Stage Files
```bash
git add .
```

### Commit Changes
```bash
git commit -m "Initial Citadel homelab commit"
```

### Add Remote Repository
```bash
git remote add origin https://github.com/blakes52897-droid/citadel-linux-lab.git
```

### Rename Branch
```bash
git branch -M main
```

### Push To GitHub
```bash
git push -u origin main
```

### Verify Sync Status
```bash
git status
```

### View Commit History
```bash
git log --oneline
```

---

# Important Git Concepts Learned

- `git add .`
  - stages modified files for commit

- `git commit`
  - creates a snapshot/checkpoint of the project

- `git push`
  - uploads local commits to GitHub

- `git status`
  - checks synchronization state between local machine and GitHub

- `working tree clean`
  - means no unsaved Git changes exist

- `origin/main`
  - refers to the GitHub remote repository branch

---

# Notes File Discovery

## Learned
Discovered there were TWO copies of `citadel-notes.md`

### Untracked Notes File
```bash
~/citadel-docs/citadel-notes.md
```

### Git-Tracked Notes File
```bash
~/citadel-linux-lab/notes/citadel-notes.md
```

## Commands Learned

### Locate Files
```bash
find ~ -iname "citadel-notes.md"
```

### Open Tracked Notes File
```bash
nano ~/citadel-linux-lab/notes/citadel-notes.md
```

---

# SSH Hardening + Key Authentication

## Completed
- Generated ED25519 SSH keypair
- Added public key to authorized keys
- Configured proper SSH permissions
- Successfully SSH'd into localhost
- Learned how encrypted remote sessions work

## Commands Learned

### Generate SSH Key
```bash
ssh-keygen -t ed25519 -C "Blake Citadel Key"
```

### View Public Key
```bash
cat ~/.ssh/id_ed25519.pub
```

### Add Public Key To Authorized Keys
```bash
cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys
```

### Secure SSH Permissions
```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

### SSH Into Local Machine
```bash
ssh localhost
```

---

# SSH Security Concepts Learned

## SSH Purpose
SSH encrypts:
- commands
- authentication
- terminal sessions
- transferred data

This protects against:
- packet sniffing
- credential theft
- session interception

## Important Realization
Logging directly into a physical machine does NOT encrypt local keyboard/display activity.

SSH specifically protects:
- network communications
- remote administration traffic

---

# SSH Hardening Troubleshooting

## Learned
- `sshd -t`
  validates SSH configuration before restart

- Syntax errors in config files can break SSH service startup

- Parse error encountered:
```text
no argument after keyword "w"
```

- Troubleshooting involved:
  - editing `/etc/ssh/sshd_config`
  - locating malformed entries
  - validating syntax safely before restarting service

## Commands Used

### Open SSH Config
```bash
sudo nano /etc/ssh/sshd_config
```

### Search Inside Nano
```text
Ctrl + W
```

### Validate SSH Config
```bash
sudo sshd -t
```

### Restart SSH Service
```bash
sudo systemctl restart ssh
```

---

# Lessons Learned

- Always verify which file is actually tracked by Git
- `git status` is one of the most important troubleshooting tools
- Validate configs BEFORE restarting services
- SSH keys are more secure than passwords
- Tiny typos in Linux configs can break services
- Version control creates safe recovery checkpoints
- Real sysadmin work involves troubleshooting, not memorization

## SSH Remote Administration Lab

### Objective
Successfully SSH into Ubuntu VM from iPhone using Termius over local network.

### Initial Issue
- SSH connection timed out from iPhone
- Ubuntu VM initially used NAT-style addressing
- SSH service was installed but inactive

### Troubleshooting Steps
- Verified VM IP with:
  ```bash
  hostname -I
  ip addr
# The Citadel Build Log

## Project
The Citadel is a self-hosted Linux security lab landing page hosted from an Ubuntu VM and exposed publicly through Cloudflare Tunnel.

Domain:
rootandrook.com

## Stack
- Windows host machine
- Oracle VirtualBox
- Ubuntu Linux VM
- Apache2 web server
- Cloudflare DNS
- Cloudflare Tunnel
- UFW firewall
- SSH enabled
- Custom HTML/CSS frontend

## Working Components
- Apache serving from /var/www/html/index.html
- Cloudflare Tunnel connected
- DNS records configured:
  - rootandrook.com
  - www.rootandrook.com
- Public HTTPS access working
- UFW enabled
- SSH allowed on port 22
- Windows sleep disabled so VM stays online

## Key Commands Used

Check Apache:
```bash
sudo systemctl status apache2
curl localhost
# THE CITADEL - SESSION NOTES
Date: 2026-05-26 / 2026-05-27

Author: Blake Swartz

====================================================
MISSION
====================================================

Goal:
Restore and stabilize The Citadel public cyber lab environment.

Domain:
rootandrook.com

Infrastructure:
- Ubuntu VM
- Apache2
- Cloudflare Tunnel
- Cloudflare DNS
- GitHub-backed project
- Docker-enabled environment
- SIEM-style telemetry interface

====================================================
PROJECT STATUS
====================================================

The Citadel is now:
- Publicly accessible
- Tunnel-connected
- GitHub committed
- Cloudflare integrated
- Persistent across sessions
- Structured as a real cyber lab portfolio project

====================================================
TECH STACK
====================================================

Host:
- Windows 11

Virtualization:
- Oracle VirtualBox

Guest OS:
- Ubuntu Linux

Web Stack:
- Apache2
- HTML
- CSS
- JavaScript

Infrastructure:
- Cloudflare Tunnel
- Cloudflare DNS
- GitHub
- Docker

Security:
- UFW Firewall
- Hardened SSH
- Fail2Ban telemetry
- Authentication logging
- SIEM-style dashboard concepts

====================================================
CLOUDFLARE CONFIGURATION
====================================================

Cloudflare successfully connected to:
rootandrook.com

DNS Records:

ROOT RECORD
Type:
CNAME

Name:
@

Target:
9d67b9ff-0fa1-402b-b0c7-9e54103e3233.cfargotunnel.com

Proxy:
Enabled

----------------------------------------------------

WWW RECORD
Type:
CNAME

Name:
www

Target:
9d67b9ff-0fa1-402b-b0c7-9e54103e3233.cfargotunnel.com

Proxy:
Enabled

====================================================
TUNNEL CONFIGURATION
====================================================

Tunnel destination:
http://localhost:80

Published Application Routes:

- rootandrook.com
- www.rootandrook.com

Catch-all rule:
http_status:404

====================================================
ERRORS ENCOUNTERED
====================================================

ERROR:
HTTP 404

CAUSE:
Tunnel routing issue.

FIX:
Reconfigured DNS and published routes.

----------------------------------------------------

ERROR:
Cloudflare Error 1016
Origin DNS error

CAUSE:
WWW record missing.

FIX:
Created explicit WWW CNAME entry.

----------------------------------------------------

ERROR:
curl: (6) Could not resolve host

CAUSE:
DNS propagation + deleted root record.

FIX:
Re-added proper DNS configuration.

----------------------------------------------------

ERROR:
Tunnel server stopped

CAUSE:
cloudflared process terminated.

FIX:
Tunnel restarted and DNS corrected.

====================================================
LINUX COMMANDS USED
====================================================

Check public response:

curl -I https://rootandrook.com

----------------------------------------------------

DNS diagnostics:

resolvectl query rootandrook.com

----------------------------------------------------

Set DNS manually:

sudo resolvectl dns enp0s3 1.1.1.1 8.8.8.8

----------------------------------------------------

Flush DNS cache:

sudo resolvectl flush-caches

----------------------------------------------------

Firewall rules:

sudo ufw allow 22/tcp
sudo ufw reload

----------------------------------------------------

Check SSH listener:

ss -tulnp | grep :22

----------------------------------------------------

Disk usage:

df -h

====================================================
WINDOWS HOST POWER CONFIGURATION
====================================================

Problem:
Windows host entered sleep mode when away from home.

Impact:
- Ubuntu VM shut down
- Apache inaccessible
- Tunnel disconnected
- Website offline

Settings changed:

Power Mode:
Best Performance

Screen Timeout:
Never

Sleep Timeout:
Never

Hibernate:
Never

Power Button:
Do Nothing

Sleep Button:
Do Nothing

====================================================
CURRENT WEBSITE STATE
====================================================

Landing page restored successfully.

Sections restored:
- Hero section
- Defense
- Monitoring
- Control
- Strategy
- Faux telemetry panels
- SIEM-style monitoring visuals
- Authentication log displays

Visual Style:
- Dark cyber aesthetic
- Grid background
- White typography
- Minimalist terminal styling
- Security operations atmosphere

Tagline:
FORTIFY THE POSITION

====================================================
SYSTEM STATUS PANEL
====================================================

Displayed metrics:

OS:
Ubuntu Linux

Hostname:
blakelinuxlab

IP:
10.0.0.10

Firewall:
ACTIVE

SSH:
HARDENED

Threat Detection:
ENABLED

Position Integrity:
STABLE

====================================================
FEATURES ALREADY IMPLEMENTED
====================================================

COMPLETED:
- Cloudflare integration
- GitHub repository integration
- Docker container environment
- SIEM-style interface
- Live authentication logs
- Public HTTPS deployment
- Firewall hardening
- SSH exposure through hardened config
- Custom telemetry panels
- Responsive public landing page
- Persistent public domain

====================================================
PROJECT STRUCTURE DISCOVERED
====================================================

Directories:

/home/blakes52897/citadel-docs

/home/blakes52897/citadel-linux-lab

/home/blakes52897/citadel-linux-lab/notes/citadel-notes.md

Backup files:
- citadel-notes-old-backup.md
- citadel-notes.md.save
- .citadel-notes.md.swp

====================================================
NEXT PHASE OBJECTIVES
====================================================

1.
Persistent cloudflared system service

2.
Dynamic real-time telemetry

3.
Grafana integration

4.
Uptime Kuma integration

5.
Containerized services expansion

6.
Real fail2ban live event feeds

7.
Security analytics dashboard

8.
Subpages:
- DEFENSE
- MONITORING
- CONTROL
- STRATEGY

9.
Mobile optimization improvements

10.
VirtualBox snapshot:
"CITADEL STABLE BUILD"

====================================================
FINAL STATUS
====================================================

The Citadel is operational.

Public URL:
https://rootandrook.com

The environment survived:
- DNS failures
- Tunnel misconfiguration
- Missing WWW records
- Cloudflare routing issues
- VM sleep interruptions
- Apache restoration
- Public deployment recovery

Current operational state:
STABLE

The tunnel lives.


Citadel Development Log - 2026-05-27

Docker + NGINX Portfolio Deployment

Objectives

* Transitioned The Citadel from a fake static telemetry dashboard into a real cybersecurity/sysadmin portfolio site
* Rebuilt frontend structure using HTML/CSS
* Containerized deployment using Docker + NGINX
* Improved overall UI/UX and project structure

⸻

Technologies Used

* Ubuntu Linux
* Docker
* NGINX
* HTML
* CSS
* Chromium
* VirtualBox

⸻

Work Completed

Docker Workflow

* Built Docker image:

sudo docker build -t citadel-site .

* Removed old container:

sudo docker rm -f citadel-site

* Deployed new container:

sudo docker run -d -p 8080:80 --name citadel-site citadel-site

⸻

Frontend Improvements

* Replaced fake telemetry dashboard
* Created professional cybersecurity portfolio homepage
* Added:
    * Navigation bar
    * Hero section
    * Project cards
    * Technology stack display
    * Styled terminal section
    * Responsive layout
    * Glassmorphism styling
    * Hover animations

⸻

Current Portfolio Sections

* Linux Hardening Lab
* Docker Web Stack
* Live Authentication Monitor
* SIEM Sandbox
* Cloudflare Remote Access
* Current Operations

⸻

Lessons Learned

* Difference between static HTML and live system telemetry
* Docker image/container lifecycle
* Importance of rebuilding containers after frontend changes
* Using:

cat > index.html <<'EOF'

to overwrite files directly from terminal

* Understanding container port conflicts
* Troubleshooting Docker container naming conflicts
* Basic frontend structure using HTML + CSS

⸻

Next Steps

* Build real project pages
* Add GitHub links
* Add LinkedIn links
* Implement live authentication log feed
* Add real Linux system telemetry
* Create documentation pages for each project
* Integrate SIEM tooling
* Continue Security+ preparation

⸻

Current Focus Areas

* Linux administration
* Security+
* Docker
* SIEM concepts
* Cloud security
* Infrastructure hardening
## 2026-05-28 - Citadel Website Enhancement

### Objective
Improve the visual presentation and professionalism of the Citadel landing page.

### Changes Made
- Fixed missing CSS brace issue that broke site styling
- Added animated glowing rook hero icon
- Improved hero section layout and spacing
- Added subtitle:
  Linux Security • Cloud • Infrastructure
- Enhanced navigation bar with blur effect and transparency
- Improved logo styling and branding
- Added smooth scrolling support
- Refined visual hierarchy of landing page
- Verified Docker container deployment
- Verified Cloudflare public access

### Skills Demonstrated
- HTML
- CSS
- Docker
- NGINX
- Linux Administration
- Git/GitHub
- Cloudflare Tunnel

### Result
Landing page now presents as a professional cybersecurity and infrastructure portfolio rather than a simple static website.
# Citadel Notes - 2026-05-29

## Phase 4 - Live Operations Dashboard

### Objective

Transform the static Operations Dashboard into a dynamic status dashboard capable of displaying live system information generated directly from the Linux host.

### Accomplishments

#### Status Generation Script

Created and tested a status generation workflow that produces a JSON file containing:

* Last update timestamp
* System uptime
* CPU load
* Memory utilization
* Disk utilization
* Docker status
* Latest Git commit

Verified output using:

```bash
curl http://localhost:8080/status.json
```

#### Dashboard Integration

Implemented JavaScript fetch functionality within the Citadel website to retrieve and display data from status.json.

Added dynamic dashboard fields for:

* Website status
* Docker status
* Latest Git commit
* Last update timestamp

Successfully validated data retrieval through browser developer tools and direct JSON access.

#### Mobile Testing

Performed testing from iPhone using:

* Local network access
* Public Cloudflare tunnel access
* RootAndRook.com production site

Confirmed dashboard functionality and responsive layout.

#### Navigation Improvements

Adjusted dashboard anchor behavior using CSS scroll-margin-top to improve mobile navigation and prevent content from hiding behind the navigation bar.

#### GitHub Integration

Implemented live commit display using data generated from the local Git repository.

Dashboard now displays latest commit hash and commit message.

Example:

8346099 - README.md

#### Production Verification

Confirmed successful operation of:

* Ubuntu Linux VM
* Docker container
* NGINX web server
* Cloudflare Tunnel
* Public domain routing
* Dynamic dashboard data

Website accessible publicly at:

https://www.rootandrook.com

### Lessons Learned

* JSON endpoints can be consumed directly from client-side JavaScript using fetch().
* Dynamic dashboards can be created without backend frameworks.
* Dockerized static sites can still present live operational data through generated JSON files.
* Cloudflare Tunnel provides secure public access without traditional port forwarding.
* Small iterative changes are easier to troubleshoot than large deployments.

### Current Citadel Status

Completed:

* Linux VM
* SSH
* UFW
* Docker
* NGINX
* Git/GitHub
* Cloudflare Tunnel
* Public Domain
* Dynamic Operations Dashboard
* Live Git Status Display

In Progress:

* Security Monitoring
* Threat Dashboard
* Authentication Telemetry
* SIEM Expansion

Project Status:
The Citadel is operational and publicly accessible.
# CITADEL NOTES UPDATE
**Date:** 2026-05-30

## Session Objective
Continue development of the Linux Hardening Lab project page, validate live dashboard telemetry, document completed security controls, and improve portfolio presentation.

---

## Security Monitoring Review

Reviewed SSH authentication logs from `/var/log/auth.log`.

Observed:

Failed password for blakes52897
Failed password for blakes52897
Accepted password for blakes52897

Confirmed:

- Remote SSH access is functioning through Cloudflare Tunnel.
- Failed authentication attempts are being logged.
- Successful authentication events are being logged.
- Authentication monitoring foundation is operational.

Evidence captured for future documentation.

---

## Authentication Monitoring Investigation

Located existing authentication monitoring components:

scripts/auth-monitor.sh
logs/auth-monitor.log
docker-site/status/auth-live.log

Reviewed:

cat scripts/auth-monitor.sh

Confirmed the environment already contained a monitoring script that:

- Watches SSH authentication events
- Writes entries to local log files
- Generates data intended for dashboard consumption

Result:

- Authentication monitoring groundwork already existed.
- Avoided duplicating functionality.
- Updated project documentation to reflect actual state.

---

## Operations Dashboard Telemetry Review

Located telemetry generation script:

cat scripts/generate-status.sh

Verified live telemetry generation for:

- Hostname
- Uptime
- IP address
- Disk usage
- Memory utilization
- Docker container count

Generated updated telemetry:

./scripts/generate-status.sh

Verified output:

cat docker-site/status/status.json

Result:

{
  "hostname": "blakelinuxlab",
  "uptime": "up 2 days, 20 hours, 21 minutes",
  "ip": "10.0.0.10",
  "disk": "27%",
  "memory": "2.9Gi / 7.3Gi",
  "containers": "1"
}

---

## Dashboard Troubleshooting

Investigated why dashboard telemetry appeared stale.

Discovered:

grep -R "status.json" docker-site

Found two separate telemetry files:

docker-site/status.json
docker-site/status/status.json

Determined:

- Operations Dashboard reads:
  docker-site/status.json

- Linux Hardening telemetry reads:
  docker-site/status/status.json

This explained inconsistent values being displayed.

---

## Docker Container Investigation

Reviewed active container:

sudo docker ps

Inspected container mounts:

sudo docker inspect citadel-site

Confirmed:

- No live bind mounts are configured.
- Site content is baked directly into the image.
- Any HTML changes require image rebuilds.

Key lesson:

Changes are not visible until the Docker image is rebuilt and redeployed.

---

## Linux Hardening Project Page Creation

Created and refined:

projects/linux-hardening.html

Connected project card:

<a href="/projects/linux-hardening.html">

Result:

- Linux Hardening Lab now has a dedicated project page.
- Portfolio projects can now expand independently from the main landing page.

---

## Linux Hardening Project Content Added

### Project Snapshot

- Started: May 2026
- Status: Active
- Public Site: rootandrook.com

### Tech Stack

- Ubuntu
- SSH
- UFW
- Fail2Ban
- Docker
- NGINX
- Cloudflare

### Project Overview

Explains:

- Remote administration
- Public hosting
- Security operations practice
- Foundation of The Citadel

### Current Capabilities

Documented:

- SSH remote access
- UFW firewall controls
- Fail2Ban deployment
- Authentication monitoring
- Dockerized hosting
- Cloudflare Tunnel
- Live Operations Dashboard telemetry

### Security Value

Documents practical skills gained through the project.

### Command Areas Practiced

systemctl status ssh

sudo ufw status verbose

journalctl -u ssh

tail -f /var/log/auth.log

sudo docker ps

### Implemented Controls

Documents security measures currently deployed.

### Next Objectives

- Integrate Fail2Ban metrics into dashboard
- Surface SSH authentication statistics
- Create authentication dashboard card
- Organize project evidence
- Build infrastructure diagrams

Removed outdated references suggesting Fail2Ban had not been implemented.

---

## Mobile Optimization Verification

Tested project page on iPhone.

Verified:

- Responsive layout
- Readable typography
- Project sections render correctly
- Navigation functions correctly

Captured screenshots for future README usage.

---

## Recommended README Screenshots

Priority images:

1. Citadel Homepage
2. Linux Hardening Project Page
3. Operations Dashboard Telemetry
4. Remote SSH Session From iPhone
5. Authentication Log Monitoring
6. Cloudflare Tunnel Access Demonstration

---

## Current Linux Hardening Lab Status

### Completed

- Ubuntu Linux deployment
- SSH configuration
- UFW firewall
- Dockerized hosting
- GitHub workflow
- Cloudflare Tunnel integration
- Public website deployment
- Fail2Ban protection
- Authentication monitoring groundwork
- Operations Dashboard telemetry
- Dedicated project page

### In Progress

- Dashboard security metrics
- Architecture diagrams
- Screenshot organization
- README polishing

### Portfolio Assessment

Linux Hardening Lab has evolved from a basic Linux setup into a documented portfolio project demonstrating:

- Linux Administration
- Remote Access Security
- Firewall Management
- Docker Operations
- Cloudflare Integration
- Git-Based Deployment
- Operational Monitoring
- Security Documentation

## Milestone Achieved

Linux Hardening Lab project page completed and integrated into The Citadel.
SSH CONFIGURATION

Verified OpenSSH server is enabled and running.

Security Settings:
- PasswordAuthentication disabled
- Keyboard-interactive authentication disabled
- SSH key authentication required
- PAM enabled for account/session management
- X11 forwarding currently enabled (candidate for future hardening)

Security Impact:
- Eliminates password-based brute force attacks
- Forces use of SSH key authentication
- Reduces attack surface for remote administration


========================================
UFW FIREWALL CONFIGURATION
========================================

Command:
sudo ufw status verbose

Current Status:
- UFW enabled and active
- Logging enabled (low)
- Default incoming policy: DENY
- Default outgoing policy: ALLOW
- Routed traffic: DENY

Allowed Rules:
- TCP/22 (SSH)
- Tailscale interface traffic (tailscale0)

Configuration:
Default: deny incoming
Default: allow outgoing
Default: deny routed

Security Impact:
- Blocks unsolicited inbound traffic by default
- Restricts public exposure to approved services only
- Allows remote administration through SSH
- Permits secure Tailscale mesh network access
- Provides baseline host firewall protection

Observed Output:

Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), deny (routed)

22/tcp ALLOW IN Anywhere
Anywhere on tailscale0 ALLOW IN Anywhere
22/tcp (v6) ALLOW IN Anywhere (v6)
Anywhere (v6) on tailscale0 ALLOW IN Anywhere (v6)

========================================
FAIL2BAN CONFIGURATION
========================================

Commands:
sudo fail2ban-client status
sudo fail2ban-client status sshd

Current Status:
- Fail2Ban service active
- SSH protection jail enabled
- Monitoring SSH authentication logs
- Automatic IP banning configured

Jails:
- sshd

Observed Statistics:
- Total failed login attempts detected: 31
- Total IP addresses banned: 3
- Currently banned: 0
- Log source: /var/log/auth.log

Security Impact:
- Detects repeated SSH authentication failures
- Automatically blocks suspicious source IPs
- Reduces risk of brute-force attacks
- Provides automated response to malicious login activity

Observed Output:

Number of Jail: 1
Jail list: sshd

Currently failed: 0
Total failed: 31

Currently banned: 0
Total banned: 3

Log source:
- /var/log/auth.log


========================================
CLOUDFLARE TUNNEL CONFIGURATION
========================================

Command:
cloudflared tunnel list

Current Tunnel:
- Name: citadel-tunnel
- Tunnel ID: 9d67b9ff-0fa1-402b-b0c7-9e54103e3233
- Created: 2026-05-26T06:09:32Z
- Active connections:
  - ord02
  - ord06
  - ord07
  - ord11

Current Version:
- cloudflared version: 2026.5.1
- Update available: 2026.5.2

Purpose:
Cloudflare Tunnel provides public access to The Citadel website without traditional router port forwarding.

Traffic Flow:
Visitor
↓
Cloudflare
↓
Cloudflare Tunnel
↓
Ubuntu Host
↓
Docker container
↓
NGINX
↓
Citadel website

Security Impact:
- Avoids opening inbound ports on the home router.
- Places Cloudflare in front of the public endpoint.
- Allows the local Docker-hosted NGINX site to be reached publicly.
- Supports a safer public exposure model for a home lab.

Recovery Notes:
If rebuilding the lab on a new VM, Cloudflare Tunnel must be reinstalled, authenticated, and configured to point back to the local Citadel service.

Observed Output:
ID: 9d67b9ff-0fa1-402b-b0c7-9e54103e3233
NAME: citadel-tunnel
CREATED: 2026-05-26T06:09:32Z
CONNECTIONS: 1xord02, 1xord06, 1xord07, 1xord11


========================================
CLOUDFLARE TUNNEL SERVICE
========================================

Command:
systemctl status cloudflared --no-pager

Service Status:
- Installed as a systemd service
- Enabled at boot
- Currently running
- Operational uptime: 3+ days

Observed Configuration:
Loaded: enabled
Active: running

Purpose:
Provides persistent secure outbound tunnel connectivity from the Ubuntu host to Cloudflare.

Benefits:
- Automatically starts after system reboot
- Maintains public website availability
- Eliminates need for router port forwarding
- Supports secure remote access architecture

Operational Validation:
Cloudflared has remained active continuously for multiple days without interruption.

Maintenance:
- Cloudflared managed through APT package repository.
- Updates performed through package management.
- Upgrade path:
  sudo apt update
  sudo apt install cloudflared

Current Version:
2026.5.1

Available Upgrade:
2026.5.2
