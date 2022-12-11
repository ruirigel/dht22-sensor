#Tasks to be run by cron

@reboot python3 /home/pi/dht22_server/dht22server.py
*/30 * * * * python3 /home/pi/dht22_server/dht22logger.py

