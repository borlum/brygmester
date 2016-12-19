#!/usr/bin/python
import serial
import glob

def sample(PORT):
    try:
        CO2SENSOR = serial.Serial(PORT, 9600)
        # Garbage
        CO2SENSOR.readline()
        # Now read!
        sample = CO2SENSOR.readline()
        # Close up
        CO2SENSOR.close()
        return int(sample)
    except Exception as e:
        print "NO CO2 SENSOR AVAILABLE..?"
        pass
    return 0