# Steps to set up a new SD card for Student Use

Written by Nick Masso in May 2021.

The source of this file is at [https://github.com/engr16x/projects-rpi-setup-6/blob/main/deploy_manual.md](https://github.com/engr16x/projects-rpi-setup-6/blob/main/deploy_manual.md) and should be edited on github first, then changes propogated to the GDrive and Eagle.

## Pre-setup

Flash the sd card with the engr16x_v6 disk image. See the "Flashing an SD card" document. You do not have to decompress the `.gz` file for the imaging software to load the image correctly. 

## During setup

1.  insert the new SD card into the raspberrypi stack you want to set up

2.  connect the ethernet cable from the raspberrypi to your computer

3.  Power on the RPi

4.  SSH into the RPi with your client of choice. 
    
    From command prompt or terminal, the command is `ssh pi@engr.local`
    
    Using putty, the host name is `engr.local`
    
5.  Log in as the `pi` user. The password is `raspberry`

    If the terminal says something about 
    
    ```
    The authenticity of host 'engr.local (fe80::bd18:7190:353e:e0ca%10)' can't be established.
    ECDSA key fingerprint is SHA256:ep88C0p1HafwD4Yoa7lnVTspSaYosj9M2x68YkNKQRc.
    Are you sure you want to continue connecting (yes/no)?
    ```
    
    type `yes` and press enter.

6.  Press the up arrow on your keyboard, this should show the command `sudo /home/pi/projects-rpi-setup-6/deploy.sh`

7.  Press enter to begin deploy.

8.  Follow the prompts on screen.

9.  When complete, enter `sudo poweroff` to safely shut down the RPi. The green `act` light on the board should flash 10 times, and on the 10th flash should hold for a second and then turn off. This is how you know the RPi has completely powered down, and it is safe to unplug it.


## Notes on using engr16x_v6

- boat update will no longer work. it should be disabled if we are replacing all OS versions with 6, or have some check for which version it is running on.

- firmware updates should be performed using the `~/Desktop/UPDATE FILES/firmware_update_[board].sh` scripts.

- elephant does not need to be run. The wifi channel randomization is preformed during setup automatically.

- file transfer should be simpler. Before trying winSCP or fileZilla, try simply copying and pasting files from your computer to the remote desktop session. The thinclient_drives directory may also show your computer's filesystem, depending on the setup. 

- Also, copying and pasting text from one computer to another should always work.

