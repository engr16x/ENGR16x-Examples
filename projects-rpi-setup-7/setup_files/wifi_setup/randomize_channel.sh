#!/bin/bash

# Short program that assigns a new WiFi channel to
# the Raspberry Pi. Then new channel number is 
# chosen randomly between 1, 6, and 11, replacing 
# the old channel number that was previously in hostapd.conf
# This aims to solve latency issues with remote desktop during
# project demos when many pis are operating on the same default
# WiFi channel. 
# Written by David Li 10/5/2020


random=$RANDOM
channels=(1 6 11)
let "randomIdx = random % 3"
let "c = channels[randomIdx]"

echo "Setting new channel to:" $c
sudo nmcli c mod pi_wifi 802-11-wireless.channel $c


