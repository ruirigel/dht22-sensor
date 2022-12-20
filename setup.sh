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

(crontab -l ; echo "@reboot cd /home/pi/dht22_server/ && python3 dht22server.py && echo "[`date "+\%d/\%b/\%Y \%H:\%M:\%S"`] Coming from the reboot." >> dht22server_log.txt") 2>&1 | grep -v "no crontab" | sort | uniq | crontab -
(crontab -l ; echo "*/30 * * * * cd /home/pi/dht22_server/ && python3 dht22logger.py && echo "[`date "+\%d/\%b/\%Y \%H:\%M:\%S"`] Logging." >> dht22server_log.txt") 2>&1 | grep -v "no crontab" | sort | uniq | crontab -
(crontab -l ; echo "59 23 * * 0 cd /home/pi/dht22_server/ && cp plot.png weather_history/plot_"`date "+\%d-\%m-\%Y_\%H:\%M:\%S"`.png" && echo "[`date "+\%d/\%b/\%Y \%H:\%M:\%S"`] Save weather history." >> dht22server_log.txt") 2>&1 | grep -v "no crontab" | sort | uniq | crontab -
(crontab -l ; echo "15 1 * * * killall -r dht22server.py && cd /home/pi/dht22_server/ && python3 dht22server.py && echo "[`date "+\%d/\%b/\%Y \%H:\%M:\%S"`] Restart server." >> dht22server_log.txt") 2>&1 | grep -v "no crontab" | sort | uniq | crontab -

echo
echo
echo "The setup has finished the procedure."
echo
echo "Enjoy!"
