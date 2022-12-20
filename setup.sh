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

(crontab -l ; echo "@reboot cd /home/$USER/dht22_server/ && echo "`hostname -I | cut -f1 -d ' '` - - [`date "+\%d/\%b/\%Y \%H:\%M:\%S"`] Coming from the reboot." >> dht22server_log.txt && python3 dht22server.py") 2>&1 | grep -v "no crontab" | sort | uniq | crontab -
(crontab -l ; echo "*/30 * * * * cd /home/$USER/dht22_server/ && python3 dht22logger.py && echo "`hostname -I | cut -f1 -d ' '` - - [`date "+\%d/\%b/\%Y \%H:\%M:\%S"`] Logging." >> dht22server_log.txt") 2>&1 | grep -v "no crontab" | sort | uniq | crontab -
(crontab -l ; echo "59 23 * * 0 cd /home/$USER/dht22_server/ && cp plot.png weather_history/plot_"`date "+\%d-\%m-\%Y_\%H:\%M:\%S"`.png" && echo "`hostname -I | cut -f1 -d ' '` - - [`date "+\%d/\%b/\%Y \%H:\%M:\%S"`] Save weather history." >> dht22server_log.txt") 2>&1 | grep -v "no crontab" | sort | uniq | crontab -
(crontab -l ; echo "15 1 * * * pkill -f dht22server && cd /home/$USER/dht22_server/ && echo "`hostname -I | cut -f1 -d ' '` - - [`date "+\%d/\%b/\%Y \%H:\%M:\%S"`] Restart server." >> dht22server_log.txt && python3 dht22server.py") 2>&1 | grep -v "no crontab" | sort | uniq | crontab -
(crontab -l ; echo "15 1 1 * * cd /home/$USER/dht22_server/ && cp dht22server_log.txt logs_history/dht22server_log_"`date "+\%d-\%m-\%Y"`.txt" && echo -n "" > dht22server_log.txt && echo "`hostname -I | cut -f1 -d ' '` - - [`date "+\%d/\%b/\%Y \%H:\%M:\%S"`] Started rotate log files." >> dht22server_log.txt") 2>&1 | grep -v "no crontab" | sort | uniq | crontab -

echo
echo
echo "The setup has finished the procedure."
echo
echo "Enjoy!"
