filename = '/etc/dnsmasq.conf'

replace = [[]]

append = ['interface=wlan0',
          '    dhcp-range=192.168.REPLACEWITHTEAMNUMBER.10,192.168.REPLACEWITHTEAMNUMBER.50,255.255.255.0,24h' ]

####################  Main Porgram  ####################

import os
from shutil import copyfile

if not(os.path.isfile(str(filename + '.orig'))):
  copyfile(filename, str(filename + '.orig'))
else:
  copyfile(str(filename + '.orig'), filename)

newfile = []

with open(filename, 'r') as file:

  for line in append:
    newfile.append(str(line + '\n'))

with open(filename, 'w') as file:
  for line in newfile:
    print(line)
    file.write(line)

copyfile(filename, str(filename + '.bak'))
