#!/bin/bash
INFOPATH="/home/pi/info.sh"
source $INFOPATH
echo "Enter the new account password:"
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

for account in ${TEAMNUMS[@]}
do
    echo "Changing $account account password"
    echo "$account:$pswd1" | chpasswd
done

echo "Password Changed"
read temp
