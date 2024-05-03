#!/bin/bash
echo
echo

runv1=0
runv2=0

while [[ $runv1 == 0 ]]; do
    read -p "Would you like to update the GrovePi firmware? (y/n) " yn
    case $yn in
        [Yy]* ) runv1=1; runv2=1; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done



if [[ $runv2 == 1 ]];
    # only update the firmware
    then
    
    # it seems like this parameter breaks avrdude's ability to flash firmaware.
    sudo raspi-config nonint do_spi 1
    cd /home/pi/Dexter/GrovePi/Firmware
    source /home/pi/Dexter/GrovePi/Firmware/grovepi_firmware_update.sh
    update_grovepi_firmware
    sudo raspi-config nonint do_spi 0
fi


echo
echo

echo "Script complete. Press [enter] to exit."

read temp
