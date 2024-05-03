#!/bin/bash

echo
echo "Downloading Files"

cd /home/pi/Desktop/updates/design-challenge
git fetch --all
git reset --hard origin/master
git pull origin master

echo
echo "Applying Updates"
sudo chown -R pi:pi /home/pi/Desktop/updates/design-challenge
sudo chmod 711 /home/pi/Desktop/updates/design-challenge/design-challenge/run.sh
sudo /home/pi/Desktop/updates/design-challenge/design-challenge/run.sh