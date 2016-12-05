BRYGMESTER
==========

Brygmester is your digital-brew-helper! It serves your by monitoring your brew and keeping you up to date with data.

For now, brygmester however only monitors temperature using the DS18B20 temperature sensor.

Brygmesters target platform is the Raspberry Pi 3 (will work on 1 and 2 as well), using [Manjaro ARM](http://manjaro-arm.org/) as the host OS.

One can just run ´python brewmon.py´ to start the beast, but it is advised to set it up as a service, which will start at boot -- thus, as little fiddling as possible.

Assuming systemd, this is done by creating a file with the following contents:

    [Unit]
    Description=Brygmester Monitor

    [Service]
    ExecStart=/path/to/brygmon.py

    [Install]
    WantedBy=multi-user.target

And saving it in /etc/systemd/system/brygmon.service. Afterwards, run:

    systemctl enable name.service

And you are good to go!