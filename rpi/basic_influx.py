#!/usr/bin/env python3

from influxdb import InfluxDBClient

database = 'sensor_data'

client = InfluxDBClient(database=database)
client.create_database(database)

data = [
    {
        "measurement": "light_sensor",
        "fields": {
            "full_flux": 12,
            "ir_flux": 6,
        }
    }
]

client.write_points(data)

result = client.query('select full_flux,ir_flux from light_sensor;')

print("Result: {0}".format(result))
