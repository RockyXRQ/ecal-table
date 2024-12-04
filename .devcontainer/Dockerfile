FROM ubuntu:22.04

# sys
RUN apt update && apt upgrade -y
RUN apt install -y software-properties-common wget build-essential

RUN apt install python3-launchpadlib -y
RUN rm -rf ~/.launchpadlib/api.launchpad.net/cache/

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py

# ecal
RUN add-apt-repository -y ppa:ecal/ecal-5.13
RUN apt update
RUN apt install -y ecal
RUN apt install -y python3-ecal5

# git
RUN apt install -y git

# protobuf
RUN apt install -y protobuf-compiler
RUN pip3 install protobuf

# numpy
RUN pip3 install numpy==1.24.4

# opencv
RUN pip3 install opencv-contrib-python-headless

# wpilib
RUN pip3 install pyntcore
RUN pip3 install robotpy-wpimath

# onnxruntime (avoid update numpy to 2.x)
RUN pip3 install onnxruntime --no-deps

# aiohttp
RUN pip3 install aiohttp

# linuxpy
RUN pip3 install linuxpy

# ruff
RUN pip3 install ruff

# v4l
RUN apt install -y v4l-utils
RUN apt install -y libv4l-dev