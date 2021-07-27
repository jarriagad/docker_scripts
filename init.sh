#!/bin/bash

#Script installs docker on Ubuntu 20.04LTS
#Make sure to run as sudo.
#GL

#Check for root
if [ "$EUID" -ne 0 ]
then 
  echo "Run as ROOT"
  exit
fi

#Install Docker

#Clean slate
apt-get remove -y docker docker-engine docker.io containerd runc

#Update apt
apt-get update -y

#Install dependencies
apt-get install -y \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg \
  lsb-release

#Add GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

#Set up stable repository
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

#Refresh apt db
apt-get update -y

#install docker packages
apt-get install -y docker-ce docker-ce-cli containerd.io


