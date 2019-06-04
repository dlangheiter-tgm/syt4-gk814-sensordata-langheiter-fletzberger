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



## Quellen

* [Adafruit RPI I2C](<https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/configuring-your-pi-for-i2c>)
* [Read TSL2561 with python](<https://github.com/ControlEverythingCommunity/TSL2561/blob/master/Python/TSL2561.py>)
* [Python Shebang line](https://stackoverflow.com/a/19305076)