#!/bin/bash

echo "###############################################"
echo "### Welcome to the dht22-sensor setup       ###"
echo "###############################################"
echo
echo
echo
echo "Setup proceeding in 10 seconds... (control-c to cancel)"
echo

sleep 10

sudo true

    sudo apt-get update
    sudo apt-get -y install \
        build-essential \
        python3 \
        python3-dev \
        python3-pip \
        gnuplot-x11
    sudo yes | python3 -m pip install --upgrade pip setuptools wheel
    sudo yes | pip3 install --install-option="--force-pi" Adafruit_DHT

echo
echo
echo "The setup has finished the procedure."
echo
echo "Enjoy!"