#!/usr/bin/python
import serial
import glob

def port():
    print(glob.glob("/dev/ttyACM*"))

def sample():
    print 22