#!/bin/bash
cd /home/pi/media-stack

# Force mount if not present
sudo mount -a

# Ensure the 'pi' user owns the data folder for Samba/Apps
sudo chown -R pi:pi ./data

git pull origin main
docker compose up -d --remove-orphans