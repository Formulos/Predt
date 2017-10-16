import sys, serial, argparse
import numpy as np
from time import sleep
from collections import deque

import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import struct

class SerialData(object):

    def __init__(self):
        self.x = [] 
        self.y = []
        self.baud_rate = 9600
        self.max_value = 20
        self.propriedade = "Corrente"

    def main(self):
        cont = 0
        arduinoData = serial.Serial("COM3",self.baud_rate)
        stuf = 20
        while cont < stuf:
        
            cont+=1
            try:
                arduinoString = arduinoData.readline()
                arduinoString = arduinoString[:-2]
                arduinoString = arduinoString.decode()            
                Data = (float(arduinoString))
                print(Data)
                self.increment(cont,Data)        
            except Exception as e:
                pass
        plt.plot(self.x,self.y,"b")
        plt.show()
        stuf +=20

    def createPlot(self):
        plt.plot(self.x)
    
    def increment(self,x,y):
        self.x.append(x)
        self.y.append(y)

    def harning():
        print("Valor acima do normal")
        

if __name__ == "__main__":
    SerialData().main()