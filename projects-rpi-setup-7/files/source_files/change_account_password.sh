#!/bin/bash
INFOPATH="/home/pi/info.sh"
source $INFOPATH
do
    echo "Enter the new account password:"
    read pswd1
    echo "Enter the same password again"
    read pswd2
done while [ "$pswd1" != "$pswd2" ]

for account in ${TEAMNUMS[@]}
do
    echo "Changing $account account password"
    echo "$account:$pswd1" | chpasswd
done