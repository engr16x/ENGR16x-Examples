#!/bin/bash

echo
echo "Downloading Files"

cd /home/pi/Desktop/updates/duck
git fetch --all
git reset --hard origin/master
git pull origin master

echo
echo "Applying Updates"
sudo chown -R pi:pi /home/pi/Desktop/updates/duck
sudo chmod 711 /home/pi/Desktop/updates/duck/duck/run.sh
sudo /home/pi/Desktop/updates/duck/duck/run.sh
