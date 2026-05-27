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
