#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run this script as root"
  exit
fi

    # For the time being this script will only work on systems with DNF as the package manager. This being Red Hat/Fedora Based Distros. 

dnf install -y python3.8 python3-pip java-latest-openjdk.x86_64 

pip install --upgrade pip

pip install -r requirements.txt

cp /service/asterion.service /usr/lib/systemd/systemd

cp /service/lavalink.service /usr/lib/systemd/systemd

systemctl enable asterion

systemctl enable lavalink

wget https://github.com/Frederikam/Lavalink/releases/latest/download/Lavalink.jar