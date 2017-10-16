import serial
import numpy
import mathplotlib.pyplot as pyplot
from drawnow import *

arduinoData = serial.Serial("com11",115200)

while True: 
    while(arduinoData.inWathing() == 0):
        pass
    arduinoString = arduinoData.readline()
    