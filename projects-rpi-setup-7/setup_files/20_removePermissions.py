# This file will remove global executable permissions from the listed files
# Those ending in a '*' will address any package starting with the preceding text
import os

path = '/usr/bin/'
# need the leading "0o" for octal conversion
newPermission = 0o700

restrict = ['apt',
            'apt-*',
            'curl',
            'dpkg',
            'dpkg-*',
            'easy_install',
            'easy_install3',
            'gem',
            'make',
            'minecraft-pi',
            'pip',
            'pip2',
            'pip3',
            'pip-3.2',
            'ruby*',
            'wget'  ]

# os.chdir('/usr/bin')

found = []
for command in os.listdir(path):
  for res in restrict:
    if (res[-1] == '*'):
      if (command.startswith(res[:-1])):
        print('Changing permissions for ', command)
        found.append(command)
    else:
      if (command == res):
        print('Changing permissions for ', command)
        found.append(command)

for f in found:
  os.chmod(os.path.join(path, f), newPermission)
  print(f, ' changed.')
