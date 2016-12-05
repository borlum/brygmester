#!/usr/bin/python
import os
import time
import csv
import logging

import brygconf
import brygsensor
import brygcloud

# Load config
config = brygconf.get()

# Open file for logging
f = open(log, 'a')
writer = csv.writer(f)

# First sleep...
time.sleep(config['SAMPLE_TIME'])
# ... Then work
while True:
    sample = brygsensor.sample()
    brygcloud.push(config['API_KEY'], config['ENDPOINT'], sample)
    time.sleep(config['SAMPLE_TIME'])
