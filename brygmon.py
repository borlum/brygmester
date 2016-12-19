#!/usr/bin/python
import os
import time

import brygconf
import brygtemp
import brygco2
import brygcloud

# Load config
config = brygconf.get()

# Setup port for CO2 sensor
port = brygco2.port()

# First sleep...
time.sleep(config['SAMPLE_TIME'])
# ... Then work
while True:
    co2 = brygco2.sample()
    temp = brygtemp.sample()

    brygcloud.push({
        'api_key': config['API_KEY'], 
        'field1': temp
    }, config['ENDPOINT'])

    time.sleep(config['SAMPLE_TIME'])