#!/usr/bin/python
import os
import time

import brygconf
import brygsensor
import brygcloud

# Load config
config = brygconf.get()



# First sleep...
time.sleep(config['SAMPLE_TIME'])
# ... Then work
while True:
    sample = brygsensor.sample()
    brygcloud.push(config['API_KEY'], config['ENDPOINT'], sample)
    time.sleep(config['SAMPLE_TIME'])