folderpath = '/home/pi/Desktop/source_files'

import os

for filename in os.listdir(folderpath):
  if (os.path.isfile(str(folderpath + '/' + filename))):
    print('Making ', str(folderpath + '/' + filename), ' executable...')
    os.chmod(str(folderpath + '/' + filename), 0o755)
