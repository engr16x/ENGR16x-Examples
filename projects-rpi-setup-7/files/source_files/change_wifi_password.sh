#!/bin/bash

echo "Enter the new wifi password (This must be no less than 8 characters):"
read pswd1
echo "Enter the same password again"
read pswd2

while [ "$pswd1" != "$pswd2" ]
do
    echo "Passwords do not match"
    echo "Enter the new account password:"
    read pswd1
    echo "Enter the same password again"
    read pswd2
done 

sudo nmcli c mod pi_wifi 802-11-wireless-security.psk $pswd1


echo "Password Changed: Please restart Pi"
echo "You may need to forget the pi wifi network on your computer to connect with new password