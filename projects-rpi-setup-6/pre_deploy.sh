#!/bin/bash

CALLDIR=`pwd`
# this should be /home/pi/$FOLDERNAME unless someone updates the name of the repository
# notice that this requires you cd into this directory before running pre_deploy
FOLDERNAME='projects-rpi-setup-6'
HOSTNAME="engr"

# making deploy executable
sudo chmod 755 ./deploy.sh

echo "Apt updating and upgrading"
sudo apt-get update --allow-releaseinfo-change-suite
sudo apt-get upgrade -y

echo "Installing and uninstalling requirenents"
# Generic dependencies
sudo apt-get install samba idle3 libncurses5 default-jdk arduino xrdp dnsmasq hostapd libffi-dev libatlas-base-dev -y

# stuff that is in the grovepi deb dependencies
sudo apt-get install --no-install-recommends -y git libi2c-dev i2c-tools \
    python-setuptools python-pip python-smbus python-dev python-serial python-rpi.gpio python-numpy python-scipy \
    python3-setuptools python3-pip python3-smbus python3-dev python3-serial python3-rpi.gpio python3-numpy python3-scipy \
    libncurses5

# get rid of these
sudo apt-get purge thonny geany -y
#sudo apt autoremove -y

# install more python libraries because they deserve it :)
sudo pip3 install numpy matplotlib pandas scipy --upgrade

# grovepi dependencies
sudo pip3 install smbus-cffi RPi.GPIO pyserial --upgrade



# Turns out apt-get install arduino is what grovepi expected. lame
#echo "Installing arduino software (not on any package managers)"
#cd /home/pi/Downloads
#sudo wget https://downloads.arduino.cc/arduino-1.8.10-linuxarm.tar.xz
#tar -xf arduino-1.8.10-linuxarm.tar.xz -v
#sudo ./arduino-1.8.10/install.sh
# notice they try to create config files in /root in a directory that doesnt exist. its fine, because we wont be using the shortcuts

echo "Installing Dexter Files"
sudo mkdir /home/pi/Dexter


# First is dexter's script_tools
sudo mkdir -p /home/pi/Dexter/lib/Dexter
cd /home/pi/Dexter/lib/Dexter
sudo git clone https://github.com/DexterInd/script_tools

# then is the RFR tools
cd /home/pi/Dexter
sudo git clone https://github.com/DexterInd/RFR_Tools.git
cd /home/pi/Dexter/RFR_Tools/miscellaneous
sudo python3 setup.py install
# this (importantly) installs wiringpi and di_i2c
# so we dont need all the extra stuff in the brickpi install script now

# next is grovepi
cd /home/pi/Dexter
sudo git clone https://github.com/DexterInd/GrovePi.git

cd /home/pi/Dexter/GrovePi/Script
sudo bash ./install.sh

# in the avrdude setup there is an error that mentions inittab
# long story short, while installing avrdude,
# they comment out and disable spawning a tty terminal on the serial port
# anything newer than wheezy (aka literally 2014) has this disabled by default.
# dont worry about it.


cd /home/pi/Dexter/GrovePi/Software/Python
sudo python3 setup.py install



# next is brickpi
cd /home/pi/Dexter
sudo git clone https://github.com/DexterInd/BrickPi3.git
cd /home/pi/Dexter/BrickPi3/Install
sudo bash ./install.sh

# install openOCD the way brickpi3 needs it
sudo curl --silent https://raw.githubusercontent.com/DexterInd/openocd/master/openocd_install.sh | bash

# add the python library to path the GOOD WAY
cd /home/pi/Dexter/BrickPi3/Software/Python
sudo python3 setup.py install



echo "Changing raspi-config settings"
# dont autologin to gui
sudo raspi-config nonint do_boot_behaviour B1
# enable comms stuff (0 is enable)
sudo raspi-config nonint do_ssh 0
sudo raspi-config nonint do_spi 0
sudo raspi-config nonint do_i2c 0
# set wifi country 
sudo raspi-config nonint do_wifi_country "US"
# set locale
sudo raspi-config nonint do_change_locale "en_US.UTF-8"
LANG="en_US.UTF-8"
sudo dpkg-reconfigure -f noninteractive locales
sudo raspi-config nonint do_change_timezone "America/New_York"
# keyboard fails. idk why
#sudo raspi-config nonint do_configure_keyboard "US"


echo "Modifying hardware permissions"
cd $CALLDIR/setup_files
sudo python3 01_config.py
sudo python3 01_modules.py
sudo python3 01_raspi-blacklist.py


echo "Changing XRDP settings"
sudo cp $CALLDIR/files/resources/loginLogo.bmp /usr/share/xrdp/logo.bmp
sudo cp $CALLDIR/files/resources/loginBackground.bmp /usr/share/xrdp/background.bmp
sudo cp $CALLDIR/files/resources/xrdp.ini /etc/xrdp/xrdp.ini


cd $CALLDIR

echo "Copying credits.txt to a better location"
cp ./files/credits.txt /home/pi/credits.txt


cd $CALLDIR/setup_files

# using our minimal installation of raspbian, we dont have these anymore
#echo "Modifying the panel"
#sudo python3 ./02_panelicons.py

echo
echo "Setting python3 to default python version"
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 2
echo
echo "Default python version is: "
python --version

echo
echo "Setting IDLE3 as default python editor"
echo "text/x-python=idle-python3.7.desktop" | sudo tee -a /usr/share/applications/defaults.list > /dev/null



echo
echo "Copying source file folder to desktop"
cp -r $CALLDIR/files/source_files/. /home/pi/Desktop/source_files/

echo "Copying newdesktop directory to pi desktop"
cp -r $CALLDIR/files/new_desktop/. /home/pi/Desktop/new_desktop/


echo "Copying Dexter examples to examples folder"
cp -r /home/pi/Dexter/BrickPi3/Software/Python/Examples/. /home/pi/Desktop/new_desktop/Examples/BrickPi3/

cp -r /home/pi/Dexter/GrovePi/Software/Python/. /home/pi/Desktop/new_desktop/Examples/GrovePi/



echo
echo "Setting up file structure to sync with github update repositories"

mkdir /home/pi/Desktop/updates
cd /home/pi/Desktop/updates

echo
echo "Setting up projects-updates/boat"
sudo rm -r boat
mkdir boat
cd boat
git init
git config core.sparsecheckout true
echo boat/ >> .git/info/sparse-checkout
git remote add -f origin https://github.com/engr16x/projects-updates.git
git pull origin master
cd ..

echo
echo "Setting up projects-updates/design-challenge"
sudo rm -r design-challenge
mkdir design-challenge
cd design-challenge
git init
git config core.sparsecheckout true
echo design-challenge/ >> .git/info/sparse-checkout
git remote add -f origin https://github.com/engr16x/projects-updates.git
git pull origin master
cd ..

echo
echo "Setting up projects-updates/donut"
sudo rm -r donut
mkdir donut
cd donut
git init
git config core.sparsecheckout true
echo donut/ >> .git/info/sparse-checkout
git remote add -f origin https://github.com/engr16x/projects-updates.git
git pull origin master
cd ..

echo
echo "Setting up projects-updates/duck"
sudo rm -r duck
mkdir duck
cd duck
git init
git config core.sparsecheckout true
echo duck/ >> .git/info/sparse-checkout
git remote add -f origin https://github.com/engr16x/projects-updates.git
git pull origin master
cd ..

echo
echo "Setting up projects-updates/elephant"
sudo rm -r elephant
mkdir elephant
cd elephant
git init
git config core.sparsecheckout true
echo elephant/ >> .git/info/sparse-checkout
git remote add -f origin https://github.com/engr16x/projects-updates.git
git pull origin master
cd ..

echo
echo "Setting up projects-updates/in-class-activities"
sudo rm -r in-class-activities
mkdir in-class-activities
cd in-class-activities
git init
git config core.sparsecheckout true
echo in-class-activities/ >> .git/info/sparse-checkout
git remote add -f origin https://github.com/engr16x/projects-updates.git
git pull origin master
cd ..

echo
echo "Setting up projects-updates/plane"
sudo rm -r plane
mkdir plane
cd plane
git init
git config core.sparsecheckout true
echo plane/ >> .git/info/sparse-checkout
git remote add -f origin https://github.com/engr16x/projects-updates.git
git pull origin master
cd ..

echo
echo "Setting up projects-updates/projects"
sudo rm -r projects
mkdir projects
cd projects
git init
git config core.sparsecheckout true
echo projects/ >> .git/info/sparse-checkout
git remote add -f origin https://github.com/engr16x/projects-updates.git
git pull origin master
cd ..









cd $CALLDIR/setup_files

echo "Making the desktop bg change script executable"
sudo chmod 755 ./21_changeBackground.sh

echo "Making source files executable"
python3 ./03_makeSourceFilesExecutable.py


# this is done earlier, i copied the code into here.
#echo "Setting up GitHub Update file structure"
#sudo ./04_setupUpdateFiles.sh



cd $CALLDIR/setup_files

echo "Changing hostname to $HOSTNAME"
sudo python3 ./05_changeHostname.py $HOSTNAME


echo "Copying modified user-facing files"
sudo cp ./06_bash_hist.txt /home/pi/.bash_history
sudo cp ./07_motd.txt /etc/motd

echo
echo "Pre-deploy setup is now complete. You may power off and image this disk."
