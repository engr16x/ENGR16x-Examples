# This file will change the program icons on the panel (programs on top bar of desktop)
import sys

orig1  = 'wolfram-mathematica.desktop'
orig2 = 'wolfram-language.desktop'

new1 = 'idle3.desktop'
new2 = 'geany.desktop'

path = str('/home/' + sys.argv[1] + '/.config/lxpanel/LXDE-pi/panels/panel')

newfile = []
with open(path, 'r') as fid:
  for line in fid:
    if str('id='+orig1) in line:
      newfile.append(line.replace(orig1, new1))
    elif str('id='+orig2) in line:
      newfile.append(line.replace(orig2, new2))
    else:
      newfile.append(line)  

with open(path, 'w') as fid:
  for line in newfile:
    fid.write(line)
