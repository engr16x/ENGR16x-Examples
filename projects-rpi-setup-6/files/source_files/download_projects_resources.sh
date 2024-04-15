#!/bin/bash

echo
echo "Downloading Files"

cd /home/pi/Desktop/updates/projects
git fetch --all
git reset --hard origin/master
git pull origin master

echo
echo "Applying Updates"
sudo chown -R pi:pi /home/pi/Desktop/updates/projects
sudo chmod 711 /home/pi/Desktop/updates/projects/projects/run.sh
sudo /home/pi/Desktop/updates/projects/projects/run.sh