#!/usr/bin/env python3

import smbus
import time

class TSL2561:
    bus_address = 0x39

    def __init__(self, integration_time=2, debounce_time=0.5):
        self.bus = smbus.SMBus(1)

        try:
            self.bus.read_byte(self.bus_address)
        except:
            raise Exception('Sensor was not found on I²C bus')

        # Power ON Mode
        self.write_byte_data(0x00 | 0x80, 0x03)

        # Set nominal integration time
        # 0 = 13.7ms; 1 = 101ms; 2 = 402ms; 3 = manual mode
        self.write_byte_data(0x01 | 0x80, integration_time)

        # Make sure sensor is ready
        time.sleep(debounce_time)

    def write_byte_data(self, cmd_reg, val):
        return self.bus.write_byte_data(self.bus_address, cmd_reg, val)

    def read_i2c_block_data(self, cmd_reg, bytes):
        return self.bus.read_i2c_block_data(self.bus_address, cmd_reg, bytes)

    @staticmethod
    def convert_data(data):
        return data[0] + data[1] * 256

    def get_data(self):
        # Read data from sensor
        data1 = self.read_i2c_block_data(0x0C | 0x80, 2)
        data2 = self.read_i2c_block_data(0x0E | 0x80, 2)

        # Convert data
        full = self.convert_data(data1)
        infrared = self.convert_data(data2)

        return full, infrared

if __name__ == '__main__':
    tsl = TSL2561()

    full, inf = tsl.get_data()

    print("Full Spectrum(IR + Visible) :%d lux" %full)
    print("Infrared Value :%d lux" %inf)
    print("Visible Value :%d lux" %(full - inf))
