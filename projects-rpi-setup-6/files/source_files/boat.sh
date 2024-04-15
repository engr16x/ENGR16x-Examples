#!/bin/bash

echo
echo "Downloading Files"

cd /home/pi/Desktop/updates/boat
git fetch --all
git reset --hard origin/master
git pull origin master

echo "Applying Updates"
sudo chown -R pi:pi /home/pi/Desktop/updates/boat/boat
sudo chmod 711 /home/pi/Desktop/updates/boat/boat/run.sh
sudo /home/pi/Desktop/updates/boat/boat/run.sh
