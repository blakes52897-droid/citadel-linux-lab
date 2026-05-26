#!/bin/bash

OUT="$HOME/citadel-linux-lab/docker-site/status/status.json"

HOSTNAME=$(hostname)
UPTIME=$(uptime -p)
IP=$(hostname -I | awk '{print $1}')
DISK=$(df -h / | awk 'NR==2 {print $5}')
MEMORY=$(free -h | awk '/Mem:/ {print $3 " / " $2}')
CONTAINERS=$(sudo docker ps -q | wc -l)

cat > "$OUT" <<EOF
{
  "hostname": "$HOSTNAME",
  "uptime": "$UPTIME",
  "ip": "$IP",
  "disk": "$DISK",
  "memory": "$MEMORY",
  "containers": "$CONTAINERS"
}
EOF
