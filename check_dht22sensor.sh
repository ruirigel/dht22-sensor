#! /bin/bash

cd /home/$USER/dht22_server/
python3 dht22logger.py
echo "`hostname -I | cut -f1 -d ' '` - - [`date "+%d/%b/%Y %H:%M:%S"`] Check sensor." >> dht22server_log.txt

