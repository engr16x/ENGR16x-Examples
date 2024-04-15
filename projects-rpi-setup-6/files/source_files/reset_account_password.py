#!/usr/bin/env python3

import getpass
import sys
import os

print('Note: Entered characters will not display on screen. \nJust type password and press [Enter].\n')

username = input('username to reset: ')
print('Updating Password for ', username, '\n')

os.system(str('yes ' + username + ' | passwd ' + username))
