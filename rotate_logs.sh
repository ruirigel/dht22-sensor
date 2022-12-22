#! /bin/bash

cd /home/$USER/dht22_server/
cp dht22server_log.txt logs_history/dht22server_log_"`date "+%d-%m-%Y"`.txt"
echo -n "" > dht22server_log.txt
echo "`hostname -I | cut -f1 -d ' '` - - [`date "+%d/%b/%Y %H:%M:%S"`] Started rotate log files." >> dht22server_log.txt

