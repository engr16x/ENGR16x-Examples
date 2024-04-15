#!/bin/bash
echo
echo

runv1=0
runv2=0
while [[ $runv1 == 0 ]]; do
    read -p "Would you like to update the brickpi3 firmware? (y/n) " yn
    case $yn in
        [Yy]* ) runv1=1; runv2=1; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done


if [[ $runv2 == 1 ]];
    # only update the firmware
    then

    cd /home/pi/Dexter/BrickPi3/Firmware
    sudo bash /home/pi/Dexter/BrickPi3/Firmware/brickpi3samd_flash_firmware.sh
fi

echo
echo

echo "Script complete. Press [enter] to exit"
read temp
