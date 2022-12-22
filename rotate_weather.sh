#! /bin/bash

cd /home/$USER/dht22_server/
cp plot.png weather_history/plot_"`date "+%d-%m-%Y"`.png"
echo "`hostname -I | cut -f1 -d ' '` - - [`date "+%d/%b/%Y %H:%M:%S"`] Rotate weather history log." >> dht22server_log.txt

