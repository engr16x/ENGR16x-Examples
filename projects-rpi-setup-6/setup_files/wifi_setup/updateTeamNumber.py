import sys
import os
from shutil import copyfile

print("NUM INPUTS: " + str(len(sys.argv)))

if (len(sys.argv) == 3):
    teamNumber = str(sys.argv[1])
    piNumber = str(sys.argv[2])
else:
    teamNumber = str(input("Enter the team number:  "))
    piNumber = str(input("Enter the Pi Number:  "))


# This might be wlan0
replaceWord = [['REPLACEWITHTEAMNUMBER', teamNumber],
           ['REPLACEWITHPINUMBER', piNumber]]

append = []
####################  Main Program  ####################


for filename in os.listdir():
  newfile = []
  with open(filename, 'r') as file:
    for line in file:
      foundReplace = False
      if (replaceWord[0][0] in line) or (replaceWord[1][0] in line):
        temp = line.replace(replaceWord[0][0], replaceWord[0][1])
        temp = temp.replace(replaceWord[1][0], replaceWord[1][1])
        newfile.append(temp)
        foundReplace = True

      if not foundReplace:
        newfile.append( line)

    for line in append:
      newfile.append(str(line + '\n'))

  with open(filename, 'w') as file:
    for line in newfile:
      file.write(line)
