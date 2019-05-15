"""
    Eddie Molina
    CSE 3313
    Spring 2018
    HW-04
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

hn_low = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]# h of n for low pass filter
hn_high = [1, -1] # h of n for high pass filter                                  

# read in images using matplotlib library
imageBoat = plt.imread("boat.512.tiff")
imageClock = plt.imread("clock-5.1.12.tiff")
imageMan = plt.imread("man-5.3.01.tiff")
imageTank = plt.imread("tank-7.1.07.tiff")
imageDarin = plt.imread("darinGrayNoise.jpg")

# convert the image data to type float
dataBoat = np.array(imageBoat, float)
dataClock = np.array(imageClock, float)
dataMan = np.array(imageMan, float)
dataTank = np.array(imageTank, float)
dataDarin = np.array(imageDarin, float)


lpFilterBoat = []
hpFilterBoat = []
for i in range(len(dataBoat)):
    cnvlvBoat1 = np.convolve(dataBoat[i], hn_low) #convolve for lowpass filter
    cnvlvBoat2 = np.convolve(dataBoat[i], hn_high)#convolve for highpass filter
    lpFilterBoat.append(cnvlvBoat1)#store convolved data in array
    hpFilterBoat.append(cnvlvBoat2)#store convolved data in array

# Display Boat images
plt.title("Boat w/o Filter")        
plt.imshow( imageBoat )
plt.show()
plt.title("Boat w/ Lowpass Filter")    
plt.imshow( lpFilterBoat )
plt.show()
plt.title("Boat w/ Highpass Filter")    
plt.imshow( hpFilterBoat )
plt.show()

lpFilterClock = []
hpFilterClock = []
for i in range(len(dataClock)):
    cnvlvClock1 = np.convolve(dataClock[i], hn_low) #convolve for lowpass filter
    cnvlvClock2 = np.convolve(dataClock[i], hn_high)#convolve for highpass filter
    lpFilterClock.append(cnvlvClock1)#store convolved data in array
    hpFilterClock.append(cnvlvClock2)#store convolved data in array

# Display Clock images
plt.title("Clock w/o Filter")        
plt.imshow( imageClock )
plt.show()
plt.title("Clock w/ Lowpass Filter")    
plt.imshow( lpFilterClock )
plt.show()
plt.title("Clock w/ Highpass Filter")    
plt.imshow( hpFilterClock )
plt.show()

lpFilterMan = []
hpFilterMan = []
for i in range(len(dataMan)):
    cnvlvMan1 = np.convolve(dataMan[i], hn_low) #convolve for lowpass filter
    cnvlvMan2 = np.convolve(dataMan[i], hn_high)#convolve for highpass filter
    lpFilterMan.append(cnvlvMan1)#store convolved data in array
    hpFilterMan.append(cnvlvMan2)#store convolved data in array

# Display Man images
plt.title("Man w/o Filter")    
plt.imshow( imageMan )
plt.show()
plt.title("Man w/ Lowpass Filter")    
plt.imshow( lpFilterMan )
plt.show()
plt.title("Man w/ Highpass Filter")    
plt.imshow( hpFilterMan )
plt.show()

lpFilterTank = []
hpFilterTank = []
for i in range(len(dataTank)):
    cnvlvTank1 = np.convolve(dataTank[i], hn_low) #convolve for lowpass filter
    cnvlvTank2 = np.convolve(dataTank[i], hn_high)#convolve for highpass filter
    lpFilterTank.append(cnvlvTank1)#store convolved data in array
    hpFilterTank.append(cnvlvTank2)#store convolved data in array

# Display Tank images
plt.title("Tank w/o Filter")    
plt.imshow( imageTank )
plt.show()
plt.title("Tank w/ Lowpass Filter")    
plt.imshow( lpFilterTank )
plt.show()
plt.title("Tank w/ Highpass Filter")    
plt.imshow( hpFilterTank )
plt.show()

outputDarin = ndimage.median_filter(imageDarin, 5) #apply median filter to image
lpFilterDarin = []
for i in range(len(dataDarin)):
    cnvlvDarin = np.convolve(dataDarin[i], hn_low) #convolve for lowpass filter
    lpFilterDarin.append(cnvlvDarin) #store convolved data in array

# Display images of Dr. Darin
plt.title("Dr. Darin w/o Filter")    
plt.imshow( imageDarin )
plt.show()
plt.title("Dr. Darin w/ Lowpass Filter")    
plt.imshow( lpFilterDarin )
plt.show()
plt.title("Dr. Darin w/ Median Filter")
plt.imshow( outputDarin )
plt.show()