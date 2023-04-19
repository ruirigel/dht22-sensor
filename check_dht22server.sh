#!/bin/bash

# 20230327 Rui Rigel

if pgrep -f "check_dht22_server.sh" > /dev/null ; then
        pkill -f check_dht22_server.sh
fi

code=$(curl --write-out %{http_code} --silent --connect-timeout 10 --output /dev/null localhost:8000/plot.png)

if [[ "$code" -ne 200 ]] ; then
	if pgrep -f "dht22server.py" > /dev/null ; then
		echo "`hostname -I | cut -f1 -d ' '` - - [`date "+%d/%b/%Y %H:%M:%S"`] Server process is running but not responding." >> dht22server_log.txt
		pkill -f dht22server
		nohup python3 dht22server.py &
	else
                echo "`hostname -I | cut -f1 -d ' '` - - [`date "+%d/%b/%Y %H:%M:%S"`] Server process is down." >> dht22server_log.txt
		nohup python3 dht22server.py &
	fi
	echo "`hostname -I | cut -f1 -d ' '` - - [`date "+%d/%b/%Y %H:%M:%S"`] Restart server." >> dht22server_log.txt
else
	exit 0
fi
