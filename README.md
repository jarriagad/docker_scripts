[![forthebadge](https://forthebadge.com/images/badges/as-seen-on-tv.svg)](https://forthebadge.com)

## This repo will be used to store all scripts related to docker.

### **FILE:** log_size_tracker.py
This script pulls the log size for containers running from a specified image name.

`./log_size_tracker.py`

Variables:
- IMAGE_NAME: name of image that was used to create containers that we want to grab logs from
- SCRIPT_LOG: Path (Absolute or relative) to .log file
- MAX_LOG_SIZE: Max size that the log file can get to before being emtied out (make sure clearing logs doesn't affect application service)

*Log file will be crated automatically if not found
*Haven't tested more than one image
*This is meant to run as cron job

Dependencies:
- Docker python SDK module

### **FILE:*** docker_init.sh
Installs Docker

`./docker_init.sh`

run as sudo

