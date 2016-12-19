#!/usr/bin/python
import os
import time
import csv

import brygconf
import brygtemp
import brygco2
import brygcloud

# Load config
config = brygconf.get()

# Sampling
devisor = (config['CLOUD_PUSH_TIME_S'] / (config['SAMPLE_TIME_MS'] * 0.001))
counter = 0

# CO2 threshold
CO2_threshold = config['CO2_ADC_THRESHOLD']
detected = 0

# CSV file log
f = open(config['CSV_LOG'], 'a')
w = csv.writer(f)

# First sleep...
time.sleep(config['CLOUD_PUSH_TIME_S'])
# ... Then work
while True:
    # SAMPLE!
    co2 = brygco2.sample(config['SER_PORT'])
    temp = brygtemp.sample()

    # Save all to CSV file
    w.writerow([int(time.time()), co2, temp])

    # CO2 threshold detector
    if co2 > CO2_threshold:
        detected = 1

    if counter % devisor:
        brygcloud.push({
            'api_key': config['API_KEY'], 
            'field1': temp,
            'field2': co2,
            'field3': detected
        }, config['ENDPOINT'])
        # Reset counter + detector
        detected = 0
        counter = 0

    # Count!
    counter = counter + 1
    time.sleep(config['CLOUD_PUSH_TIME_S'])