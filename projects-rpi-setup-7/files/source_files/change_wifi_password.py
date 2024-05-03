#!/usr/bin/env python3

# This is the start of the line containing the password in the hostapd.conf file
passwdLine = 'wpa_passphrase='
# Location of the file with the password
filePath = '/etc/hostapd/hostapd.conf'


with open(filePath, 'r') as file:
    for line in file:
        if line.startswith(passwdLine):
            oldPass = line[len(passwdLine):-1]

validPassword = False

while(not validPassword):
    if (input("Enter Current Passord:  ") == oldPass):
        while(not validPassword):
            newPassword = input("Enter New Password:  ")
            if (newPassword.find(' ') == -1):
                validPassword = True
            else:
                print("Passwords can not contain spaces.")
    else:
        print("Invalid Password")

newFile = []
if validPassword:
    with open(filePath, 'r') as file:
        for line in file:
            print(line)
            if line.startswith(passwdLine):
                line.replace(oldPass, newPass)
            newFile.append(line)
    input(' ')

    with open(filePath, 'w') as file:
        for line in newFile:
            print(line)
            file.write(line)

    print("Password Changed.")
    input(' ')
