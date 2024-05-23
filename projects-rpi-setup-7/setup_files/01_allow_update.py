filename = '/etc/polkit-1/localauthority/50-local.d/46-allow-update-repo.pkla'

append = ['[Allow Package Management all Users]\n',
          'Identity=unix-user:*\n',
          'Action=org.freedesktop.packagekit.system-sources-refresh\n',
          'ResultAny=yes\n',
          'ResultInactive=yes\n',
          'ResultActive=yes\n']

####################  Main Porgram  ####################

import os
import sys
from shutil import copyfile

with open(filename, 'w') as file:
  for line in append:
    file.write(str(line))