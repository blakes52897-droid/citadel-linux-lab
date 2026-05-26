#!/bin/bash

echo "THE CITADEL STATUS"
echo "Hostname: $(hostname)"
echo "Uptime: $(uptime -p)"
echo "IP Address: $(hostname -I)"
echo "Docker Containers:"
sudo docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
echo "Disk Usage:"
df -h /
echo "Memory:"
free -h
