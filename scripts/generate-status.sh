#!/bin/bash

OUT="$HOME/citadel-linux-lab/docker-site/status.json"

UPDATED=$(date '+%Y-%m-%d %H:%M:%S')
UPTIME=$(uptime -p)
CPU_LOAD=$(uptime | awk -F'load average: ' '{print $2}')
MEMORY=$(free -m | awk '/Mem:/ {print $3 "MB / " $2 "MB"}')
DISK=$(df -h / | awk 'NR==2 {print $5}')
DOCKER=$(sudo docker ps --filter "name=citadel-site" --filter "status=running" -q | grep -q . && echo "running" || echo "stopped")
LAST_COMMIT=$(git log -1 --pretty=format:'%h - %s')

cat > "$OUT" <<EOF
{
  "updated": "$UPDATED",
  "uptime": "$UPTIME",
  "cpu_load": "$CPU_LOAD",
  "memory": "$MEMORY",
  "disk": "$DISK",
  "docker": "$DOCKER",
  "last_commit": "$LAST_COMMIT"
}
EOF
