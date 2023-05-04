# Dockerfile

# Author       : MythDeath
# Github       : https://github.com/MythDeath
# Messenger    : Yok
# Email        : "X"
# Date         : 25-08-2021
# Main Language: Python

# Download and import main images

# Operating system
FROM debian:latest
# Main package
FROM python:3

# Author info
LABEL MAINTAINER="https://github.com/KasRoudra/PyPhisher"

# Working directory
WORKDIR PyPhisher/
# Add files 
ADD . /PyPhisher

# Installing other packages
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install php openssh-client -y
RUN pip3 install -r files/requirements.txt
RUN apt-get clean

# Main command
CMD ["python3", "pyphisher.py", "--noupdate"]

MythDeath/pyphisher"
