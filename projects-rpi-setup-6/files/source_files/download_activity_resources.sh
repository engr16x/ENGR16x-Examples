#!/bin/bash

echo
echo "Downloading Files"

cd /home/pi/Desktop/updates/in-class-activities
git fetch --all
git reset --hard origin/master
git pull origin master

echo
echo "Applying Updates"
sudo chown -R pi:pi /home/pi/Desktop/updates/in-class-activities
sudo chmod 711 /home/pi/Desktop/updates/in-class-activities/in-class-activities/run.sh
sudo /home/pi/Desktop/updates/in-class-activities/in-class-activities/run.sh
