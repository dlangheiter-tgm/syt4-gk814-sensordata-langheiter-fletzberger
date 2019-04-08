# Industrial Programming "Anzeige und Analyse von Sensordaten" - Taskdescription

## Einführung
Die Theorieeinheiten dienen als Einführung in die Verwendung von Single-Board-Computern zur Aufnahme und Verarbeitung von Sensordaten.

## Ziele
Das Ziel ist es eine geeignete Schnittstelle zur Aufnahme von Sensordaten auszuwählen. Die Daten sollen aggregiert und zur weitern Verarbeitung bearbeitet bzw. angezeigt werden.

## Voraussetzungen
* Verwendung von Mikrokontrollern und Single-Board-Computern (SBC)
* Einsatz einer persönlichen Micro-SD Karte
* Kenntnis einer hardwarenahen Programmiersprache
* Grundverständnis von digitalen Systemen
* Grundkenntnisse über die sichere Verwendung von Elektronikbauteilen

## Detailierte Aufgabenbeschreibung
Es soll ein LaTeX-Protokoll [1] erstellt werden, das folgende Themengebiete abdeckt:

+ Auswahl und Gegenüberstellung von Kommunikationsschnittstellen [2]
+ Programmierung und Konfiguration eines Single-Board-Computers
+ Aufnahme von Sensordaten
+ Verarbeitung und Aggregation der Daten und entsprechende Anzeige dieser [3, 4]

Die Themenschwerpunkte sollen soweit erläutert und mit Quellen versehen werden, sodass ein leichter Einstieg und eine mühelose Verwendung der einzelnen Tools und der Hardware gegeben ist.

Es soll ein Sensor gewählt werden, dessen Daten kontinuierlich mittels eines Single-Board-Computers (SBC) verarbeitet werden. Dabei ist zu beachten, dass gewisse zeitliche Kriterien zu erfüllen sind. Die Verarbeitung der Daten ist erst im erweiterten Teil zu implementieren. Vorerst sollen nur die Sensordaten mit unterschiedlichen Methoden ausgelesen und gespeichert werden.

## Abgabe
Das Protokoll ist als PDF-Dokument abzugeben und als doppelseitig-beidseitiger (gespiegelt an der langen Kante) Ausdruck vorzulegen. Die entsprechenden Konfigurationsdateien und Deployment-Anweisungen sind im README.md festzuhalten. Etwaiger Programmcode zur Sensordaten-Verarbeitung ist ebenfalls hier zu dokumentieren.

## Bewertung
Gruppengrösse: 1-2 Personen
### Grundanforderungen **überwiegend erfüllt**
- [ ] Dokumentation und Beschreibung anhand der Protokollrichtlinien
- [ ] Vergleich von seriellen Kommunikationsschnittstellen bei Single-Board-Computern (SBC)
- [ ] Konfiguration und Inbetriebnahme eines SBCs
- [ ] Aufnahme und einfache Archivierung von Sensordaten
### Grundanforderungen **zur Gänze erfüllt**
- [ ] Verarbeitung und entsprechende Aggregierung von Sensordaten
- [ ] Weitergabe der Sensordaten an entsprechende externe Schnittstellen
### Erweiterte Anforderungen **überwiegend erfüllt**
- [ ] Installation eines time-series Datastores
- [ ] Verwendung einer webbasierten, grafischen Anzeige der Sensordaten
### Erweiterte Anforderungen **zur Gänze erfüllt**
- [ ] automatisierte Funktionsüberprüfung
- [ ] Warnmeldung bei Überschreiten von vordefinierten Schwellenwerten


### Quellen
[1] LaTeX template [online](https://github.com/TGM-HIT/latex-protocol)
[2] "Serial Communications Methods via GPIO"; MBTechWorks; last visited: 2019-04-08; [online](https://www.mbtechworks.com/hardware/raspberry-pi-UART-SPI-I2C.html)  
[3] "InfluxDB - open source time series platform" [online](https://github.com/influxdata/influxdb)  
[4] "Grafana Labs - The open platform for beautiful analytics and monitoring" [online](https://grafana.com/)  
