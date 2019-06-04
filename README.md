# Industrial Programming "Anzeige und Analyse von Sensordaten"

## Aufgabenstellung
Die detaillierte [Aufgabenstellung](TASK.md) beschreibt die notwendigen Schritte zur Realisierung.

## Recherche

[Pdf Protocol](./syt4_gk814_sensordata_langheiter_fletzberger.pdf)

[Overleaf Project Link](https://www.overleaf.com/read/kcnqzgbjykym)

## Implementierung und Konfiguration

```bash
sudo apt-get install python-smbus python3-smbus
sudo apt-get install i2c-tools
```

By running  ` sudo i2cdetect -y 1` (it could be `0` for you) we can search for attached I²C devices.

```
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- 39 -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

### Install InfluxDB

This was written on 04.06.2019. For up-to-date install procedures please referee to the [official website](<https://www.influxdata.com/>).

Add InfluxDB repository key

```bash
curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
```

Load `VERSION_ID` variable

```bash
source /etc/os-release
```

Install the right version.

```bash
test $VERSION_ID = "7" && echo "deb https://repos.influxdata.com/debian wheezy stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
test $VERSION_ID = "8" && echo "deb https://repos.influxdata.com/debian jessie stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
test $VERSION_ID = "9" && echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
```

Update local repositories and install InfluxDB

```bash
sudo apt update
sudo apt install influxdb -y
```

Start InfluxDB

```bash
sudo systemctl unmask influxdb.service
sudo systemctl start influxdb
```

To check if everything works enter `influx` into the CLI. You should see something similar to this:

```
Connected to http://localhost:8086 version 1.7.6
InfluxDB shell version: 1.7.6
Enter an InfluxQL query
> 
```

With `exit` you can stop the program.

### Install InfluxDB python library

Install with command:

```bash
sudo apt install python3-infuxdb
```

### Running the programms

All programs are written in Python3. They are all capable to be run by bash directly.

#### Programs:

##### basicRead.py

Is the program directly taken from controleverything

##### read.py

Is a class to be used to read data from the sensor

##### basic_influx.py

Is a testing file to test the connection to InfluxDB

##### continuous_read.py

Is the first implementation of using `read.py` and Influx. It reads the sensor every second and stores it into the InfluxDB.

The wait time between read/writes can be changed by supplying an argument which specifies the save interval in seconds.

```bash
./continuous_read.py 0.1 # Reads the sensor every 0.1 Seconds
```

###  Install Grafana

Check the [official grafana website](<https://grafana.com/grafana/download?platform=arm>) for updated install specifics.

```bash
wget https://dl.grafana.com/oss/release/grafana-rpi_6.2.1_armhf.deb 
sudo dpkg -i grafana-rpi_6.2.1_armhf.deb
```

The last step failed. I fixed it by using:

```bash
sudo apt upgrade
sudo apt --fix-broken install
```

Enable Grafana service and start it

```bash
sudo systemctl enable grafana-server.service
sudo service grafana-server start
```

After this you should be able to access grafana by accessing the IP of the Pi with the port `3000`. The default credentials are `admin` : `admin`.

After that I added a data source. As we install InfluxDB I choose InfluxDB as type. I left everything as default expect `database`. There I entered `sensor_data` as per the program.

After that I hit `Save & Test`. If you see the error message `database not found: sensor_data` just start the `continuous_read.py` and at least wait until you see the message `Initializing sensor...`. Then try again.

Then you can create your first Visualization (the small bar graph on the top right). Then select Graph. Then go to queries (on the left the 4 Symbols the top one). Remove all `group by` statements by clicking on `time` and then remove. Click on `select measurement` and select `light_sensor`. Click under `field(value)` on `value` and select `full_flux`. Then press the `+` just to the right. Select under `Fields` `field`. In the new line change `full_flux` to `ir_flux`. Then hit the right arrow in the top left corner to go back to the dashboard. There you should se you visualization.

## Quellen

* [Adafruit RPI I2C](<https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/configuring-your-pi-for-i2c>)
* [Read TSL2561 with python](<https://github.com/ControlEverythingCommunity/TSL2561/blob/master/Python/TSL2561.py>)
* [Python Shebang line](https://stackoverflow.com/a/19305076)
* [Check Sensor is present](<https://www.raspberrypi.org/forums/viewtopic.php?t=114401#p782496>)
* [InfluxDB RPi](<https://gist.github.com/boseji/bb71910d43283a1b84ab200bcce43c26>)
* [InfluxDB Python](<https://github.com/influxdata/influxdb-python>)
* [Grafana](https://grafana.com/)

