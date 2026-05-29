#!/bin/bash

OUT="$HOME/citadel-linux-lab/docker-site/status.json"

CPU_LOAD=$(uptime | awk -F'load average:' '{ print $2 }' | xargs)
MEM_USED=$(free -m | awk '/Mem:/ {print $3}')
MEM_TOTAL=$(free -m | awk '/Mem:/ {print $2}')
DISK_USED=$(df -h / | awk 'NR==2 {print $5}')
UPTIME=$(uptime -p)
DOCKER_STATUS=$(sudo docker inspect -f '{{.State.Status}}' citadel-site 2>/dev/null || echo "not running")
LAST_COMMIT=$(git -C "$HOME/citadel-linux-lab" log -1 --pretty=format:'%h - %s')
UPDATED=$(date '+%Y-%m-%d %H:%M:%S')

cat > "$OUT" <<EOF
{
  "updated": "$UPDATED",
  "uptime": "$UPTIME",
  "cpu_load": "$CPU_LOAD",
  "memory": "${MEM_USED}MB / ${MEM_TOTAL}MB",
  "disk": "$DISK_USED",
  "docker": "$DOCKER_STATUS",
  "last_commit": "$LAST_COMMIT"
}
EOF
