filename = '/etc/NetworkManager/system-connections/pi_wifi.nmconnection'

replace = [[]]

append = 'address1=192.168.REPLACEWITHTEAMNUMBER.10,192.168.REPLACEWITHTEAMNUMBER.50'

####################  Main Porgram  ####################

import os
from shutil import copyfile

if not(os.path.isfile(str(filename + '.orig'))):
  copyfile(filename, str(filename + '.orig'))
else:
  copyfile(str(filename + '.orig'), filename)

newfile = []

with open(filename, 'r') as file:

  for line in file:
    newfile.append(str(line + '\n'))
    if(line.strip() == 'method=shared'):
      newfile.append(append)

with open(filename, 'w') as file:
  for line in newfile:
    print(line)
    file.write(line)

copyfile(filename, str(filename + '.bak'))
