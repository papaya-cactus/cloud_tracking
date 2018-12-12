import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import cm
import cv2
from numpy import unravel_index
import os
import re

with open('combined.txt') as f:
    lines = f.readlines()
    y = [line.split()[1] for line in lines]
    #y = [line.split()[1] for line in lines]

x = []

for i in range(0,len(y)):
    x.append(5*i + 5)    
            
plt.plot(x,y, label = 'Horn-Schunk')
plt.xlabel('Lead-time, s')
plt.ylabel('Forecast accuracy, %')
plt.legend()
plt.show()
