filename = '/proc/sys/net/ipv4/ip_forward'

####################  Main Porgram  ####################

import os
from shutil import copyfile

if not(os.path.isfile(str(filename + '.orig'))):
  copyfile(filename, str(filename + '.orig'))
else:
  copyfile(str(filename + '.orig'), filename)

newfile = []


with open(filename, 'w') as file:
  file.write('1')
