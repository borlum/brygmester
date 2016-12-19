BRYGMESTER
==========

Brygmester is your digital-brew-helper! It serves your by monitoring your brew and keeping you up to date with data.

For now, brygmester however only monitors temperature using the DS18B20 temperature sensor.

Brygmesters target platform is the Raspberry Pi 3 (will work on 1 and 2 as well), using [Manjaro ARM](http://manjaro-arm.org/) as the host OS.

Brygmester, for now, relies on a 3rd party data-handling API, [ThingSpeak](https://thingspeak.com). This may change -- but it makes it easy to bootstrap projects, and ThingSpeak seems pretty reliable for hobby data-needs.

SETUP
=====
To get up and running, one must create an account at ThingSpeak and setup a new channel (where you will push your data to). When you have created a channel, you must go to the API keys tab, and copy the *Write API Key*. Now, setup a brygmester config file as so:

    cp config.json.template config.json

Alter the *API KEY* entry in `config.json` to the one copied from ThingSpeak. **Optionally**, change the sample time.

Now, one can just run `python brewmon.py` to start the beast, but it is advised to set it up as a service, which will start at boot -- thus, as little fiddling as possible.

Assuming systemd, this is done by creating a file with the following contents:

    [Unit]
    Description=Brygmester Monitor

    [Service]
    ExecStart=/path/to/brygmon.py

    [Install]
    WantedBy=multi-user.target

And saving it in /etc/systemd/system/brygmon.service. Afterwards, run:

    systemctl enable brygmon.service

And you are good to go!

TROUBLESHOOT
============
Adding support for OneWire in RaspberryPi; modify `/boot/config.txt` by adding the following line at the bottom:
    
    dtoverlay=w1-gpio

With the CO2 serial module (read: Arduino-hacked-as-serial-ADC), one may run into permission problems reading from serial. Make sure you have added yourself to uucp group by:
    
    usermod -a -G uucp yourregusername

Extra, [wiring up the DS18B20 with Raspberry Pi basics (..)](https://www.modmypi.com/blog/ds18b20-one-wire-digital-temperature-sensor-and-the-raspberry-pi).