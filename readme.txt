# Dependencies
dht22 sensor, raspberry pi, distribution derived from Debian (raspbian), $gnuplot and $python3

# Tasks to be run by cron
@reboot python3 /home/pi/dht22_server/dht22server.py
*/30 * * * * python3 /home/pi/dht22_server/dht22logger.py

