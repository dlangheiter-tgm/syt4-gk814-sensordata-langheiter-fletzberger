#!/usr/bin/env python3

from influxdb import InfluxDBClient
import sys
import time
from read import TSL2561

database = 'sensor_data'
save_interval = 1
error_counter = 0
max_errors = 10

if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            save_interval = float(sys.argv[1])
        except ValueError:
            print('First parameter should be a number. Got "{}"'.format(sys.argv[1]))
            sys.exit(-1)

    print('Connecting to database...')

    db = InfluxDBClient(database=database)
    db.create_database(database)

    print('Initializing sensor...')
    sensor = TSL2561()

    print('Start reading data...')

    try:
        while True:
            try:
                full, ir = sensor.get_data()
                insert = [
                    {
                        "measurement": "light_sensor",
                        "fields": {
                            "full_flux": full,
                            "ir_flux": ir,
                        }
                    }
                ]
                db.write_points(insert)
                print('Inserted data: Flux: Full: {}; Infrared: {}'.format(full, ir))
                error_counter = 0
            except OSError:
                print('Got error while reading sensor. Continuing...')
                error_counter += 1
                if error_counter > max_errors:
                    print('To many continuous errors. Stopping')
                    sys.exit(-2)

            time.sleep(save_interval)
    except KeyboardInterrupt:
        print('User Interrupt. Stopping...')
