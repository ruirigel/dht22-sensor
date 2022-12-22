#!/bin/bash

cd /home/$USER/dht22_server/
echo "`hostname -I | cut -f1 -d ' '` - - [`date "+%d/%b/%Y %H:%M:%S"`] Check." >> dht22server_log.txt

if ! [ $(curl -LI `hostname -I | cut -f1 -d ' '`:8000 -o /dev/null -w '%{http_code}\n' -s) == "501" ]; then
        if pgrep -x "dht22server.py" >/dev/null; then
                pkill -f dht22server.py
                echo "`hostname -I | cut -f1 -d ' '` - - [`date "+%d/%b/%Y %H:%M:%S"`] Restart server." >> dht22server_log.txt
                python3 dht22server.py
        else
                echo "`hostname -I | cut -f1 -d ' '` - - [`date "+%d/%b/%Y %H:%M:%S"`] Start server." >> dht22server_log.txt
                python3 dht22server.py
        fi
fi


