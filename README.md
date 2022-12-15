# dht22-sensor
Created out of the need to monitor atmospheric conditions within a astronomical observatory.
The project dht22-sensor is small service to show atmospheric conditions by sensor dht22

### Features
* By http protocol we can see the values in CSV format or in graphic.
* Dew Point calculations.

### Requirements
* Raspberry Pi with Raspbian OS
* Mini Breadboard wire
* DHT22 Humidity Sensor
* One 10k ohm resistor (Brown, Black, Orange, Gold)

## Hardware Setup
### DHT22 sensor pinout 
```
Pin 1 is VCC (Power Supply)
Pin 2 is DATA (Data signal)
Pin 3 is NULL (Do not connect)
Pin 4 is GND (Ground)
```
### Raspberry Pi DHT22 Circuit
```
Place a 10k resistor between Pin 1 and Pin 2 of the DHT22
Wire Pin 1 of the DHT22 to Physical Pin 1 (3v3) on the Pi 
(for the use of 3v the wire must be equal or less than one meter)
Wire Pin 2 of the DHT22 to Physical Pin 7 (GPIO4) on the Pi
Wire Pin 4 of the DHT22 to Physical Pin 6 (GND) on the Pi
```
## Installation of dht22-sensor project
1. Install git.
```
apt-get install git
```
2. Clone the dht22-sensor git repository.
```
git clone https://github.com/ruirigel/dht22-sensor.git
```
3. Navigate to the dht22-sensor sub-directory.
```
cd dht22-sensor/
```
4. Run setup.sh to install the relevant software.
 * Note:  You may be prompted for a password for sudo.
 ```
chmod +x setup.sh
```
```
./setup.sh
```
### Manual operation
1. Edit crontab to insert tasks to be run by cron.
```
crontab -e
```
Insert these two lines. First line starts the service at boot up, the second line every 30 minutes consults the sensor
and third line copies the graph of the week every Sunday.
Change the USER in lines and (ctrl+x) to save.
```
@reboot cd /home/<USER>/dht22_server/ && python3 dht22server.py
*/30 * * * * cd /home/<USER>/dht22_server/ && python3 dht22logger.py
59 23 * * 0 cd /home/<USER>/dht22_server/ && cp plot.png weather_history/plot_"$(date '+%m%d%Y').png"
```
2. Start dht22-sensor server.
```
sudo reboot now
```
3. Open the addresses in your browser.
```
http://localhost:8000/dhtvalues
http://localhost:8000/plot.png
```
Congratulations if you seeing this similar result: https://github.com/ruirigel/dht22-sensor/blob/main/plot.png
