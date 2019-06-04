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



## Quellen

* [Adafruit RPI I2C](<https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/configuring-your-pi-for-i2c>)
* [Read TSL2561 with python](<https://github.com/ControlEverythingCommunity/TSL2561/blob/master/Python/TSL2561.py>)
* [Python Shebang line](https://stackoverflow.com/a/19305076)
* [Check Sensor is present](<https://www.raspberrypi.org/forums/viewtopic.php?t=114401#p782496>)
* [InfluxDB RPi](<https://gist.github.com/boseji/bb71910d43283a1b84ab200bcce43c26>)
* [InfluxDB Python](<https://github.com/influxdata/influxdb-python>)