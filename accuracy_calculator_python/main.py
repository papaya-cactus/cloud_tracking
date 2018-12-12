import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import cm
import cv2
from numpy import unravel_index
import os
import re

# Helper functions rgb2intensity, findsun, circle
# Main functions are segmentation and comparison
# Segmentation takes a rgb image as input and outputs a 2D array, with each element containing info about whether it is sky, cloud or undefined 
# Input 2 images (their corresponding arrays) into the comparison function and it outputs accuracy (of forecast vs actual) 

# Function to convert rgb image to intensity by simply using r+g+b
def rgb2intensity(rgb):
    return np.dot(rgb[...,:3], [1, 1, 1])

# Find Sun in the image, as we do not want to confuse the Sun with clouds since they both give similar values after normalizing b-r
def findsun(imagee):

    im = Image.open(imagee)
    img = np.array(im)

    grey = rgb2intensity(img)

    maximum = grey.max()

    sun = unravel_index(grey.argmax(), grey.shape)

    if maximum > 750:
        return sun
    
    else:
        return False
    
# Function to identify which pixels are severely affected by the Sun, radius = 170 has been set arbitrarily
def circle(x,y,midx,midy,radius):
    distance = np.sqrt( (abs(x-midx))**2 + (abs(y-midy))**2 )
    
    if distance < radius:
        return True
    else:
        return False
        
# Main function to segment image into sky, cloud and undefined
def segmentation(imagename):                

    im = Image.open(imagename)
    img = np.array(im)

    [midx,midy] = findsun(imagename)

    radius = 170

    for i in range(0,1286):
        for j in range(0,1286):
            if img[i][j][0] < 15 and img[i][j][1] < 15 and img[i][j][2] < 22: # This condition for undefined has been set arbitrarily too
                img[i][j] = [255,0,0]
            if circle(i,j,midx,midy,radius): # Condition for Sun, which we consider as undefined too
                img[i][j] = [255,0,0]
                                  
    new_image = [[0 for x in range(1286)] for y in range(1286)]
    bar_array = []

    for i in range(0,1286):
        for j in range(0,1286):        
            ratio = (float(img[i][j][2]) - float(img[i][j][0]))/(float(img[i][j][2]) + float(img[i][j][0])) # Using (b-r)/(b+r) gives us the best result currently 
            bar_array.append(ratio)
        
            if ratio == -1:
                new_image[i][j] = 155 # Undefined, grey
            
            else:
                if ratio > 0.25:
                    new_image[i][j] = 255 # Sky, white
                else:                
                    new_image[i][j] = 5 # Clouds, black
    
    #plt.figure(1)
    #plt.hist(bar_array, bins=256) # This histogram tells us the cutoff is 0.25. Again, more work can be done to decide on a better cut off
    #plt.show()                
                                                    
    #plt.figure(2)
    #plt.imshow(new_image, cmap = plt.get_cmap('gray')) # This figure shows grey, white and black areas in accordance to the criteria earlier
    #plt.show()
    
    return new_image

# Function to compare two images (e.g. forecast vs actual)and subsequently output prediction accuracy

def comparison(image1,image2):
    same = []
    different = []
    undef = []

    for i in range(0,1286):
        for j in range(0,1286):
            if image1[i][j] == 155 or image2[i][j] == 155:
                undef.append(1)
            else:
                if image1[i][j] == image2[i][j]:
                    same.append(1)
                else:
                    different.append(1)
    
    a = float(len(same))
    b = float(len(different))
    c = float(len(undef))                
                                                    
    accuracy = a/(a+b)
    
    return accuracy*100        

def main(imagename1,imagename2): # Note input should be a string 
  
    image1 = segmentation(imagename1)  
    image2 = segmentation(imagename2)

    return comparison(image1,image2)

# Code to combine and run the functions

def run():
    actual = [] 
    forecast = []  
    accuracy = [] 

    images = os.listdir('.')  # This only works when directory is set to target folder
    
    
    for i in range(0,len(images)):
        if images[i].find('actual') != -1:
            actual.append(str(images[i]))
        
        if images[i].find('forecast') != -1:
            forecast.append(str(images[i]))
    
    leadtime = 490
  
    for i in range(0,len(actual)):
        for j in range(0,len(forecast)):
            
            number = re.findall(r'\d+', actual[i])
            
            result = number[0] in forecast[j]
            
            if result == True:
                accuracy.append(main(actual[i],forecast[j]))
                                
                leadtime += 5
                
                myfile = open('results_2.txt', 'a')
                myfile.write("%f %f \n" % (float(leadtime), float(main(actual[i],forecast[j]))))  
                
                
    return accuracy
    



def plotgraph():
    accuracies = run()  
   
    leadtime = []
    
    for i in range(0,len(accuracies)):
        leadtime.append(5 + (5*i))
    
    plt.plot(leadtime, accuracies)
    plt.xlabel('Lead time, s')
    plt.ylabel('Accuracy, %')
    plt.show()
        