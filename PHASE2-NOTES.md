# Phase 2 - Defensive Hardening & Public Exposure
Date: 2026-05-26

---

# Objectives
- Publicly expose the Citadel lab safely
- Harden SSH access
- Implement intrusion prevention
- Add live telemetry and monitoring
- Simulate hostile authentication attempts
- Verify automated defensive response

---

# Infrastructure Stack

## Core Environment
- Ubuntu Linux VM
- Apache2 web server
- SSH remote administration
- Cloudflare Tunnel
- Cloudflare Zero Trust
- Fail2Ban intrusion prevention
- Docker-hosted Citadel dashboard

---

# Cloudflare Tunnel Deployment

## Completed
- Installed and authenticated cloudflared
- Created tunnel:
  - `citadel-tunnel`
- Verified healthy connector status
- Connected public hostname:
  - `rootandrook.com`
- Routed HTTP traffic to local Apache instance on port 80
- Removed restrictive Access authentication for public viewing
- Confirmed remote browser accessibility

## Lessons Learned
- Cloudflare Access policies can unintentionally lock down public portfolio pages
- Tunnel connectors remained healthy even while routing configuration was incorrect
- Public hostname routing required correct HTTP service mapping

---

# Citadel Dashboard Development

## Added Features
- Live system telemetry
- Dynamic uptime display
- Hostname visibility
- IP visibility
- Memory usage metrics
- Disk usage metrics
- Running container count
- Threat detection status
- Firewall status
- SSH hardening indicators

## Frontend Improvements
- Improved responsive mobile scaling
- Added live authentication telemetry panel
- Added defense-monitor section
- Added periodic auto-refresh behavior
- Cleaned telemetry display formatting

---

# Fail2Ban Deployment

## SSH Protection Enabled
- Configured Fail2Ban jail for SSH
- Verified auth.log monitoring
- Verified polling backend operation
- Tested brute-force detection manually

## Debugging Performed
- Investigated missing fail events
- Verified regex matching with:
  - `fail2ban-regex`
- Confirmed auth.log parsing functionality
- Determined self-originating traffic was ignored due to:
  - `ignoreself`

## Key Discovery
Fail2Ban intentionally ignored attacks originating from the same host:
```text
Ignore 10.0.0.10 by ignoreself rule

