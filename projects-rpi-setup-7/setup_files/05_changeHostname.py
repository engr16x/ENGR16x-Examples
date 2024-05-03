# This file will make sure the hostname is fully changed
from os.path import isfile
from shutil import copyfile
from sys import argv

hostname = argv[1]
files = ['/etc/hostname', '/etc/hosts']

print('New Hostname: ', hostname)

for filename in files:
  if not(isfile(str(filename + '.orig'))):
    copyfile(filename, str(filename + '.orig'))

  newfile = []
  with open(filename, 'r') as fid:
    for line in fid:
      newfile.append(line.replace('raspberrypi', hostname))

  with open(filename, 'w') as fid:
    for line in newfile:
      fid.write(line)
