#!/bin/bash
#Script to Update From Github and Restart Asterion Bot

git pull origin beta

pip install -r requirements.txt

systemctl restart asterion