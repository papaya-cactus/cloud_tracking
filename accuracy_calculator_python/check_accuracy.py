import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import cm
import cv2

"""
im = plt.imread('0124_Cropped.jpg')

plt.figure()
plt.imshow(im, interpolation="none")


plt.show()

x = [[0 for i in range(im.shape[0])] for j in range(im.shape[1])]

for ii in range (1,im.shape[0]):
    for jj in range(1,im.shape[1]):
        x[ii][jj] = im[ii][jj]

"""
                
im = Image.open('0124_Cropped.jpg')

im2 = im.convert('RGBA')



data = np.array(im2)   
red, green, blue, alpha = data.T 

cloud_areas = (red < 15) & (blue < 22) & (green < 15)
data[..., :-1][cloud_areas.T] = (255, 0, 0) 

im3 = Image.fromarray(data)
im3.show()

"""
img = cv2.imread('0124_Cropped.jpg', -1)

color = ('b','g','r')
for channel,col in enumerate(color):
    histr = cv2.calcHist([img],[channel],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.title('Histogram for color scale picture')
plt.show()
"""
