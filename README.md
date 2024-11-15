The project is constantly being updated until the first realise is created.
thank you.

# dht22-sensor
Created out of the need to monitor atmospheric conditions within a astronomical observatory.
The project dht22-sensor is small service to show atmospheric conditions by sensor dht22

![](./plot.png)
![](./csv.png)

### Features
* By http protocol we can see the values in CSV format or in generated graphic.
* Temperature
* R.Humidity
* Dew Point
* Heat index 
* Weather history

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

![](./IMG_20230409_142613_194~2.jpg)


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
1. Start dht22-sensor server.
```
sudo reboot now
```
2. After reboot open the addresses in your browser.
```
http://localhost:8000/dht22values
http://localhost:8000/plot.png
```
Congratulations if you seeing this similar result: https://github.com/ruirigel/dht22-sensor/blob/main/plot.png


### Updates
```
cd dht22-sensor
```
```
git pull origin main
```
The git pull command will download the changes and automatically merge them into your local copy. This is useful for keeping the code updated with the latest changes made to the remote repository.
