#!/bin/bash
#Script to Update From Github and Restart Asterion Bot

git pull origin beta

systemctl restart asterion