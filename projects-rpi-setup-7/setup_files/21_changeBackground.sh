#!/bin/bash

echo
echo "Updating desktop settings..."

USERNAME=$1
CONFDIR=/home/$USERNAME/.config
FILEDIR=/home/pi/projects-rpi-setup-7/files/resources

mkdir -p $CONFDIR/pcmanfm/LXDE-pi/      # desktop-items-0.conf
mkdir -p $CONFDIR/gtk-3.0/              # settings.ini
mkdir -p $CONFDIR/lxsession/LXDE-pi/    # desktop.conf

cp $FILEDIR/purdue-* /usr/share/rpd-wallpaper/
cp $FILEDIR/desktop-items-0.conf $CONFDIR/pcmanfm/LXDE-pi/
cp $FILEDIR/settings.ini $CONFDIR/gtk-3.0/
cp $FILEDIR/desktop.conf $CONFDIR/lxsession/LXDE-pi/

# set IDLE3 as the default editor, but for real this time ig
# cp $FILEDIR/mimeapps.list $CONFDIR/

echo "Desktop settings updated."
echo