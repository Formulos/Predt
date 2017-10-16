import sys, serial, argparse
import numpy as np
from time import sleep
from collections import deque
import plot.py
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
    

# main() function
def main():
    
    # Plot parameters
    analogPlot = AnalogPlot(strPort, 1000)

    print('plotting data...')

    # Set up animation
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 1000), ylim=(0, 10230))
    a0, = ax.plot([], [])
    a1, = ax.plot([], [])
    anim = animation.FuncAnimation(fig, analogPlot.update, 
                                    fargs=(a0, a1), 
                                    interval=50)

    # Show plot
    plt.show()
    
    # Clean up
    analogPlot.close()

if __name__ == '__main__':
  main()