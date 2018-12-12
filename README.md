The algorithms in this file allow one to:

1) Calculate the optical flow between two frames, and utilize such a flow to forecast the third image via warping. The optical flow method being used is the Horn-Schunck method.
2) Once a forecasted image is obtained, one can then compare this image with an actual image to calculate the forecasting accuracy. 

Usage for 1) is by runnning runflow.m for a pair of images, whereas main.m can be used to automate the running for many images.

Usage for 2) is by calling the main() function in main.py, whereas the run() function in main.py automates this process for many images. 

Eg: One can input the example images given, actual_DSC_9251.jpg and actual_DSC_9253.jpg, to obtain forecast_DSC_9255.jpg by using 1). This foreacsted image can then be compared with actual_DSC_9255.jpg using 2). 
