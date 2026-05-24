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
- Repeated failed login attempts can trigger automatic bans
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
