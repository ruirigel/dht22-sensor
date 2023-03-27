#! /bin/bash

cp plot.txt plot_history/plot_"`date "+%d-%m-%Y"`.txt"
echo -n "" > plot.txt
echo "`hostname -I | cut -f1 -d ' '` - - [`date "+%d/%b/%Y %H:%M:%S"`] Started rotating plot files." >> dht22server_log.txt
