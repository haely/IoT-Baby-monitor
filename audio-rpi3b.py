# Contributors:
# Haely Shah
# Ryan K

import wiringpi as wpi


import time
wpi.wiringPiSetup()
"""
import RPi.GPIO as GPIO
import re, sys
import RPi.GPIO as rpi
from smbus import SMBus
from time import sleep
from math import sin, fabs
if needed
"""

# GPIO pin setup
# Gate digital o/p is 1 when sound is detected #29 in odroid
# Envelope is the analog o/p #40 in odroid: gpio 17 in Josiah's sms code, 21 here
# Haely TODO : jeez idk how its 21 and 17. gl explaining this to your advisor - R

wpi.pinMOde(21, 40 here(change to 21,17))
while True:
	i = wpi.digitalRead(21)
	if i == 0:
		print("no sound', i)
	elif i == 1:
		print('Sound detected', i)
	time.sleep(60)
	
# try this once that works: for analog
while True:
   i=wpi.analogRead(0)  #adc-ain0
   ampl = i*255/2047 # not sure this is correct
   if ampl <= 10:
       print ("quiet: ", ampl, ", ", i)
   elif ampl <= 30:
       print ("moderate: ", ampl, ", ", i)
   else:
       print ("loud: ", ampl, ", ", i)
   time.sleep(60)
