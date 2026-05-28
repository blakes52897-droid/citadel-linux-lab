#!/bin/bash

cd ~/citadel-linux-lab || exit 1

git fetch origin main

LOCAL=$(git rev-parse main)
REMOTE=$(git rev-parse origin/main)

if [ "$LOCAL" != "$REMOTE" ]; then
  echo "New changes found. Deploying Citadel..."
  git pull origin main

  cd docker-site || exit 1

  sudo docker build -t citadel-site .
  sudo docker rm -f citadel-site
  sudo docker run -d -p 8080:80 --name citadel-site citadel-site

  echo "Citadel deployed."
else
  echo "No changes."
fi
