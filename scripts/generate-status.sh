#!/bin/bash

PROJECT_DIR="/home/blakes52897/citadel-linux-lab"
OUT="$PROJECT_DIR/docker-site/status.json"

cd "$PROJECT_DIR" || exit 1

UPDATED=$(date '+%Y-%m-%d %H:%M:%S')
UPTIME=$(uptime -p)
CPU_LOAD=$(uptime | awk -F'load average: ' '{print $2}')
MEMORY=$(free -m | awk '/Mem:/ {print $3 "MB / " $2 "MB"}')
DISK=$(df -h / | awk 'NR==2 {print $5}')

APACHE=$(systemctl is-active apache2 2>/dev/null || echo "unknown")
CLOUDFLARED=$(systemctl is-active cloudflared 2>/dev/null || echo "unknown")
FAIL2BAN=$(systemctl is-active fail2ban 2>/dev/null || echo "unknown")
TAILSCALE=$(systemctl is-active tailscaled 2>/dev/null || echo "unknown")
DOCKER=$(systemctl is-active docker 2>/dev/null || echo "unknown")

DOCKER_CONTAINERS=$(docker ps --format '{{.Names}}' 2>/dev/null | wc -l)
FAILED_UNITS=$(systemctl --failed --no-legend 2>/dev/null | wc -l)
SSH_FAILED_TODAY=$(grep "$(date '+%b %e')" /var/log/auth.log 2>/dev/null | grep -i "failed password" | wc -l)
FAIL2BAN_BANNED=$(sudo fail2ban-client status sshd 2>/dev/null | awk -F: '/Currently banned/ {gsub(/[[:space:]]/,"",$2); print $2}')
LAST_COMMIT=$(git log -1 --pretty=format:'%h - %s' 2>/dev/null || echo "unknown")

[ -z "$FAIL2BAN_BANNED" ] && FAIL2BAN_BANNED="unknown"

cat > "$OUT" <<EOF
{
  "updated": "$UPDATED",
  "uptime": "$UPTIME",
  "cpu_load": "$CPU_LOAD",
  "memory": "$MEMORY",
  "disk": "$DISK",
  "services": {
    "apache": "$APACHE",
    "cloudflared": "$CLOUDFLARED",
    "fail2ban": "$FAIL2BAN",
    "tailscale": "$TAILSCALE",
    "docker": "$DOCKER"
  },
  "security": {
    "ssh_failed_today": "$SSH_FAILED_TODAY",
    "fail2ban_banned": "$FAIL2BAN_BANNED",
    "failed_systemd_units": "$FAILED_UNITS"
  },
  "docker": {
    "running_containers": "$DOCKER_CONTAINERS"
  },
  "last_commit": "$LAST_COMMIT"
}
EOF
