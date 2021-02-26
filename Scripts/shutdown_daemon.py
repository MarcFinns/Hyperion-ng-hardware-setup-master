#!/usr/bin/python
#-------------------------------------------------------------------------------
# Name:         Shutdown Daemon
#
# Purpose:      This program gets activated at the end of the boot process by
#               cron. (@ reboot sudo python /home/pi/shutdown_daemon.py)
#               It monitors a button press. If the user presses the button, we
#               Halt the Pi, by executing the poweroff command.
#
#               The power to the Pi will then be cut when the Pi has reached the
#               poweroff state (Halt).
#               To activate a gpio pin with the poweroff state, the
#               /boot/config.txt file needs to have :
#               dtoverlay=gpio-poweroff,gpiopin=27
#
# Author:      Paul Versteeg
#
# Created:     15-06-2015, revised on 18-12-2015
# Copyright:   (c) Paul 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BCM) # use GPIO numbering
GPIO.setwarnings(False)

# I use the following two GPIO pins because they are next to each other,
# and I can use a two pin header to connect the switch logic to the Pi.
INT = 6    # GPIO-6 button interrupt to shutdown procedure

# use a weak pull_up to create a high
GPIO.setup(INT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main():

    while True:
        # set an interrupt on a falling edge and wait for it to happen
        GPIO.wait_for_edge(INT, GPIO.FALLING)

        subprocess.call(['poweroff'], shell=True, \
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if __name__ == '__main__':
    main()
    
