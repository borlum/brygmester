#!/usr/bin/python
import json

def get(file = 'config.json'):
    try:
        with open(file) as content:
            return json.load(content)
    except IOError as e:
        print "Is there a config file? =>", e