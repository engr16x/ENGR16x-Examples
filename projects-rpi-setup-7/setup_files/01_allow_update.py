filename = '/etc/polkit-1/localauthority/50-local.d/46-allow-update-repo.pkla'

append = ['[Allow Package Management all Users]',
          'Identity=unix-user:*',
          'Action=org.freedesktop.packagekit.system-sources-refresh',
          'ResultAny=yes',
          'ResultInactive=yes',
          'ResultActive=yes']

####################  Main Porgram  ####################

import os
import sys
from shutil import copyfile


if not(os.path.isfile(str(filename + '.orig'))):
  copyfile(filename, str(filename + '.orig'))
elif os.path.isfile(str(filename)):
  copyfile(str(filename + '.orig'), filename)


with open(filename, 'w') as file:
  for line in append:
    file.write(line)

copyfile(filename, str(filename + '.bak'))
