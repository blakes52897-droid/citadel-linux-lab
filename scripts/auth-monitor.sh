#!/bin/bash

journalctl -u ssh -f | while read line
do
    echo "$(date '+%H:%M:%S') | $line" \
    >> ~/citadel-linux-lab/logs/auth-monitor.log

    tail -n 20 \
    ~/citadel-linux-lab/logs/auth-monitor.log \
    > ~/citadel-linux-lab/docker-site/status/auth-live.log
done
