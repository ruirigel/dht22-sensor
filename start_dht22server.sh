#! /bin/bash

cd /home/$USER/dht22_server/
echo "`hostname -I | cut -f1 -d ' '` - - [`date "+%d/%b/%Y %H:%M:%S"`] Coming from the reboot." >> dht22server_log.txt
python3 dht22server.py
