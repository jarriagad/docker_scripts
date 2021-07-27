#!/usr/bin/env python3


#This is used to keep track of the size of the streetmechant01 container (log) size

import docker
import os
import logging

SCRIPT_LOG = '/var/log/SCRIPT_LOG.log'
IMAGE_NAME = 'ghcr.io/jef/streetmerchant:nightly'
MAX_LOG_SIZE = 300
client = docker.from_env()
all_containers = client.containers.list()

#find the given image
for i in all_containers:
    config_dir = i.attrs.get("Config")
    loaded_image = config_dir['Image']
    if loaded_image == IMAGE_NAME:
        log_path = i.attrs.get("LogPath")
        dir_size = os.path.getsize(log_path)
        dir_size_mb = round(dir_size / 1024 / 1024, 3)

#Create log file to keep track of size
logging.basicConfig(filename=SCRIPT_LOG, filemode='a', format='%(asctime)s: %(levelname)s - %(message)s', level=logging.DEBUG)
log_msg = "Log size: %sMb" % (dir_size_mb)
logging.info(log_msg)

#Clean out log if size exceeds determined max
if dir_size_mb > MAX_LOG_SIZE:
    file = open(log_path,"w")
    file.close()
    print("Log file has been terminated")
    logging.warning("Log has been deleted")
