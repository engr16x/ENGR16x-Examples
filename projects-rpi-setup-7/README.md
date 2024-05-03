# projects-rpi-setup-6
Setup files for student RPIs version 6. Planned release Fall 2021.

[![forthebadge](https://forthebadge.com/images/badges/you-didnt-ask-for-this.svg)](https://forthebadge.com)

## Team Lead History

Name | Term | Non-Purdue Email
--- | --- | ---
Nick Masso | Fall 2019 - Spring 2021 | nmasso@protonmail.com
Trevor Ladner | Fall 2021 - Spring 2022 | tjmladner@yahoo.com

NOTE: issue tracking will be done in the [Github Issues tab](https://github.com/engr16x/projects-rpi-setup-6/issues) so that people can pick tasks, make comments, and make pull requests. This file will simply give an overview of all the things we mean to tackle.

## Changes

The first thing that needs to be done is give a new group of TAs an understanding of the RPI setup. This will create a deeper understanding of these systems.

We should refactor the current code to make it more understandable at a glance. We will also add several fixes and improvements. Trevor made his existing code very modular and its written mostly in Python, and I only made small changes to bring us to v5.3. 

### Why Version 6?

Big reason: I would like to change the setup scripts. Most of our RPI setup documentation has a specific series of instructions that work for 5.2 and 5.3, but would not be applicable after this revision. Big number change would really emphasize this.

## Large Fixes

### Fix Broadcast IP address 3rd octet (192.168.XXX.1) having to be 2 OR 3 digit number

This is a problem that first appeared in fall 2017, where Trevor Meyer rolled out engrOS v5.2.
After deploy_wifi.sh, we were just unable to use the IP address to connect to RPIs that had a single-digit
3rd octet. Using engr.local worked fine, but not all students will have hostname resolution
on their computers. The workaround was to use three digits, 10X for dingle digit teams.

If I had to take a guess, this is something to do with /etc/dhcpcd.conf or /etc/hostapd.conf. 
Definitely worth poking around in those areas, and checking out what changes are made to them
during deploy_wifi.

### Restructure the deploy.sh scripts

There are a series of changes that would make the deploy script better.

- require internet connectivity to start
- Remove some uneccesary printing - pipe some output to files for debugging
- don’t re-enter team number and kit number after deploying wifi

### Reevaluate Dexter's Software

Lets check out how Trevor applied the Dexter software, and what the most minimal way could be.
Obviously we dont need some of the other folders, like the plain brickpi, and the new
grovepi requires the RFR stuff. So theres some changes we could do. 

I know from updating the brickpi libaries that things can be even simpler than we were doing it - lots of things are more low-level and can work better when we manage them carefully.

## Trivial fixes

### change ./Desktop/setup_files/wifi_setup/updateTeamNumber.py to accept 3 digit numbers

We already do this workaround during setup for single-digit teams. This is also more of
a future-proofing thing. The check should be that the value is between 0 and 255 inclusive.

### Make wifi broadcast channel randomized

This fix is already done in David Li's Elephant update. Modify the channel line in 
/etc/hostapd.conf, and during setup we use random to do this. We could make it deterministic,
and use like a mod of the team+pi number.

### Add Default File association for .py to IDLE3

This has gotta be a flag somewhere to be done on command line.

### Ultrasonic Sensor CM -> MM

Some old documentation (pre-2017) for this class references a file called firmwareUpdate.sh on the rpi desktop that changes the ultrasonic to MM instead of CM. I have never seen this file, and I would love that to work.

### Automatically change desktop background

There should probably be a way to change the desktop background WITHOUT an active x-window. Trevor nor I were able to find a solution, so we have that step where we log in via remote desktop to run that like 5-line script.

If there is no way to do this without an active window, we can probably put a line in the file that starts the GUI. startx can execute some basic code, and we can probably change it to check what the background is, and change it if it is not the one we want. This would push the desktop bg change to the first time anyone logs in via remote desktop, so when the pi is already in the student's hands.

### Dont auto-login as Pi user when connected to monitor

We dont want any clever students getting ideas. This is a single line to add to setup.

### Create dedicated firmware update scripts

I'm sick of having to release a new BOAT update that covers a billion edge cases for all RPis that have been in use for the last like 3 years. These firmware updates will work for exactly the software this device ships with, and will never go to a newer or older version. This image is locked to a specific, functional build.

### Add attribution file

We should get credit for doing things. We are using a student's own designed background, and he should get credit too. This file is a chance to wax poetic about our place in the general impermanence of the universe.

### Store setup data on the RPI.

I want to be able to ask the RPi when it was created, what team it is, what accounts are on it, etc. This is a powerful diagnostics tool.
