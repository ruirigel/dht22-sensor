#!/bin/bash

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
        gnuplot

    sudo yes | python3 -m pip install --upgrade pip setuptools wheel
    sudo yes | pip3 install --install-option="--force-pi" Adafruit_DHT

(crontab -l ; echo "@reboot cd /home/$USER/dht22_server/ && python3 dht22server.py") 2>&1 | grep -v "no crontab" | sort | uniq | crontab -
(crontab -l ; echo "*/30 * * * * cd /home/$USER/dht22_server/ && python3 dht22logger.py") 2>&1 | grep -v "no crontab" | sort | uniq | crontab -
(crontab -l ; echo "59 23 * * 0 cd /home/$USER/dht22_server/ && ./rotate_weather.sh") 2>&1 | grep -v "no crontab" | sort | uniq | crontab -
(crontab -l ; echo "*/5 * * * * cd /home/$USER/dht22_server/ && python3 check_dht22server.py") 2>&1 | grep -v "no crontab" | sort | uniq | crontab -
(crontab -l ; echo "15 1 1 * * cd /home/$USER/dht22_server/ && ./rotate_logs.sh") 2>&1 | grep -v "no crontab" | sort | uniq | crontab -
(crontab -l ; echo "15 1 1 * * cd /home/$USER/dht22_server/ && ./rotate_plot.sh") 2>&1 | grep -v "no crontab" | sort | uniq | crontab -

chmod +x rotate_weather.sh rotate_plot.sh rotate_logs.sh

echo
echo
echo "The setup has finished the procedure."
echo
echo "Enjoy!
