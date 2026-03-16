#!/bin/bash
cd /home/pi/media-stack

# Check for updates from Git
git pull origin main

# Create folders if they don't exist
mkdir -p data/media/tv data/media/audiobooks data/torrents config

# Ensure the 'pi' user (1000) owns the data
sudo chown -R 1000:1000 ./data ./config

# Start the containers
docker compose up -d --remove-orphans
