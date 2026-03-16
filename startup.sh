#!/bin/bash
# Move to the directory where the repo is cloned
cd "$(dirname "$0")"

# Update from Git
git pull origin main

# Force create necessary folders if they got deleted
mkdir -p data/media/tv data/media/audiobooks data/media/podcasts data/torrents config/sonarr config/qbittorrent config/audiobookshelf config/postgres

# IMPORTANT: Fix permissions for the 'pi' user so Docker doesn't fail
sudo chown -R $USER:$USER .
sudo chmod -R 775 .

# Fire up the containers
docker compose up -d --remove-orphans
