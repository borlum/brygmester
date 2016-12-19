#!/usr/bin/python
import glob
import os
import time

try:
    # Load GPIO driver
    os.system('modprobe w1-gpio')
    # Load temperature sensor driver
    os.system('modprobe w1-therm')
   # Location of sensors
    base_dir = '/sys/bus/w1/devices/'
    # The first available temperature sensor (folder)
    device_folder = glob.glob(base_dir + '28*')[0]
    # The first available temperature sensor (file)
    device_file = device_folder + '/w1_slave'
except Exception as e:
    print "Device not detected"
    pass

def get_device_output():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def sample(testing = False):
    if testing:
        return 11.562

    # Read driver
    lines = get_device_output()
    
    # Sample output:
    # af 00 4b 46 7f ff 01 10 81 : crc=81 YES
    # af 00 4b 46 7f ff 01 10 81 t=10937

    # If no 'YES' at end line 1, then there is no reading available
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()

    # When we have a reading available;
    # Read the digits after t= on the second line
    pos = lines[1].find('t=')
    if pos != -1:
        temperature_string = lines[1][pos + 2:]
        temperature_celcius = float(temperature_string) / 1000.0
        return temp_c