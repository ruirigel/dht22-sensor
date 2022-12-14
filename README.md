# dht22-sensor
Created out of the need to monitor atmospheric conditions within a astronomical observatory.
The project dht22-sensor is small service to show atmospheric conditions by sensor dht22

## Features
* By http protocol we can see the values in CSV format or in graphic
* Dew Point calculations.
 
## Requirements
* Raspberry Pi with Raspbian OS
* Mini Breadboard wire
* DHT22 Humidity Sensor
* One 10k ohm resistor (Brown, Black, Orange, Gold)

## Installation
1. Install git
```
apt-get install git
```
2. Clone the dht22-sensor git repository
```
git clone https://github.com/ruirigel/dht22-sensor.git
```
3. Navigate to the dht22-sensor sub-directory
```
cd dht22-sensor/
```
4. Run setup.sh to install the relevant software
 * Note:  You may be prompted for a password for sudo
```
./setup.sh
```

### Manual operation
1. Edit crontab to insert tasks to be run by cron.
```
crontab -e
```
Insert these two lines. First line starts the service at boot up, the second line every 30 minutes consults the sensor. 
Change the USER in lines and (ctrl+x) to save.

```
@reboot cd /home/<USER>/dht22_server/ && python3 dht22server.py >> output.log
*/30 * * * * cd /home/<USER>/dht22_server/ && python3 dht22logger.py >> output.log
```
2. Start dht22-sensor server
```
sudo reboot now
```
