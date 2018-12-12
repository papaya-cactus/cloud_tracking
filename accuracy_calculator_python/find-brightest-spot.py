import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import cm
import cv2
from numpy import unravel_index

def rgb2intensity(rgb):
    return np.dot(rgb[...,:3], [1, 1, 1])

def findsun(imagee):

    im = Image.open(imagee)
    img = np.array(im)

    grey = rgb2intensity(img)

    maximum = grey.max()
    
    print maximum

    sun = unravel_index(grey.argmax(), grey.shape)

    if maximum > 750:
        return sun
    
    else:
        return False
    