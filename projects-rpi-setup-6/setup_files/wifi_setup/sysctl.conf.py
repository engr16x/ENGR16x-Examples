filename = '/etc/sysctl.conf'

replace = [['#net.ipv4.ip_forward=1', 'net.ipv4.ip_forward=1']]

append = ['']

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
    foundReplace = False
    for phrase in replace:
      if phrase[0] in line:
        newfile.append( line.replace(phrase[0], phrase[1]))
        foundReplace = True
        break

    if not foundReplace:
      newfile.append( line)

  for line in append:
    newfile.append(str(line + '\n'))

with open(filename, 'w') as file:
  for line in newfile:
    file.write(line)

copyfile(filename, str(filename + '.bak'))

