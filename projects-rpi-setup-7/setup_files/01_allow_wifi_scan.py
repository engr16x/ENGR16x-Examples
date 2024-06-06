filename = '/etc/polkit-1/localauthority/50-local.d/47-allow-wifi-scan.pkla'

append = ['[Allow Wifi Scan]\n'
          'Identity=unix-user:*\n'
          'Action=org.freedesktop.NetworkManager.wifi.scan;org.freedesktop.NetworkManager.enable-disable-wifi;org.freedesktop.NetworkManager.settings.modify.own;org.freedesktop.NetworkManager.settings.modify.system;org.freedesktop.NetworkManager.network-control\n'
          'ResultAny=yes\n'
          'ResultInactive=yes\n'
          'ResultActive=yes\n']

####################  Main Porgram  ####################

import os
import sys
from shutil import copyfile

with open(filename, 'w') as file:
  for line in append:
    file.write(str(line))