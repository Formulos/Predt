import sys, serial, argparse
import numpy as np
from time import sleep
from collections import deque
from drawnow import *
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import struct

class SerialData(object):

    def __init__(self):
        self.propriedade       = "Corrente"
        self.criticalValue     = 0.06
        self.baud_rate         = 9600
        self.max_value         = 20
        self.yPlotLim          = [-0.05,0.12]
        self.xPlotLim          = [0,20] 
        self.x                 = [] 
        self.y                 = []    
        self.lineLim           = []
        plt.ion()
    
    def main(self):    
        arduinoData = serial.Serial("COM3",self.baud_rate)
        numberCont = 0
        self.createLimite()

        while True:
            try:
                arduinoString = arduinoData.readline()
                Data = self.getValue(arduinoString)
                numberCont += 1
                self.increment(numberCont,Data)
                
                if (len(self.y) > self.max_value):
                    self.y.pop(0)
                
                if (self.y[-1] > self.criticalValue):
                    self.harning() 
            
            except Exception as e:
                print(e)
            drawnow(self.createPlot)               

    def getValue(self, arduinoString):
        arduinoString = arduinoString[:-2]
        arduinoString = arduinoString.decode()            
        return  float(arduinoString)
        
    def createLimite(self):
        for i in range(self.max_value):
            self.lineLim.append(self.criticalValue)

    def harning(self):
        print(self.propriedade, "fora do normal")
    
    def createPlot(self):
        plt.title("Análise de Propriedade")
        plt.grid(True)
        plt.ylabel(self.propriedade)
        plt.ylim(self.yPlotLim[0],self.yPlotLim[1])
        plt.xlim(self.xPlotLim[0],self.xPlotLim[1])
        plt.plot(self.lineLim, label = "Valor critico")
        plt.plot(self.y, label = self.propriedade)
        plt.legend(loc='upper right')
    
    def increment(self,x,y):
        self.x.append(x)
        self.y.append(y)

if __name__ == "__main__":
    SerialData().main()