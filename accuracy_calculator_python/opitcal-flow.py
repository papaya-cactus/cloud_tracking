import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2

image1 = np.array(Image.open('DSC_0124.JPG'))
image2 = np.array(Image.open('DSC_0125.JPG')) 

image1G = cv2.cvtColor(image1, cv2.COLOR_RGB2GRAY)
image2G = cv2.cvtColor(image2, cv2.COLOR_RGB2GRAY) 

flow = cv2.calcOpticalFlowFarneback(image1G, image2G, flow=None,pyr_scale=0.5, levels=1, winsize=15,iterations=2,poly_n=5, poly_sigma=1.1, flags=0)


h, w = flow.shape[:2]
flow = -flow
flow[:,:,0] += np.arange(w)
flow[:,:,1] += np.arange(h)[:,np.newaxis]
result = cv2.remap(image1G, flow, None, cv2.INTER_LINEAR) 

plt.imshow(result)
plt.show()