import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import cm
import cv2

def create_circular_mask(h, w, center=None, radius=None):

    if center is None: # use the middle of the image
        center = [int(w/2), int(h/2)]
    if radius is None: # use the smallest distance between the center and image walls
        radius = min(center[0], center[1], w-center[0], h-center[1])

    Y, X = np.ogrid[:h, :w]
    dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[1])**2)

    mask = dist_from_center <= radius
    return mask

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

im = Image.open('0124_Cropped.jpg')    
img = np.array(im)

grey = rgb2gray(img)
            
h, w = grey.shape[:2]
mask = create_circular_mask(h, w,[1000,200],170)

#print create_circular_mask(h, w,[1000,200],170)
#masked_img = img.copy()
#masked_img[mask] = [255,0,0]

plt.figure(3)
#plt.imshow(masked_img) 
#plt.show()

#masked_img_final = img.copy()
masked_img_final = [[0 for x in range(1286)] for y in range(1286)]

for i in range(0,1286):
    for j in range(0,1286):
        if mask[i][j] == True:
            masked_img_final[i][j] = 255
        else:
            masked_img_final[i][j] = grey[i][j]

#plt.imshow(masked_img_final)
plt.imshow(masked_img_final, cmap = plt.get_cmap('gray'))
plt.show()    

print masked_img_final[800][1000]         