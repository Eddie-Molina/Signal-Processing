"""
    Eddie Molina
    CSE 3313-001
    Spring 2018
    HW-04
"""
import numpy as np
import csv
import matplotlib.pyplot as plt

# Variables
fs = 2000       # sampling rate frequency
fc_low = 50     # cut off for low frequency
fc_high = 280   # cut off for high frequency
ft_low = fc_low / fs    # normalized low cut off frequency
ft_high = fc_high / fs  # normalized high cut off frequency
L = 21      # filter length
M = L - 1   # filter length - 1

# read in the data from csv file
with open('data-filtering.csv', 'r') as csvfile:
    readData = csv.reader(csvfile, delimiter = ',')
    for i in readData:
        data = i
        length = len( i ) # length to the total numbers in the file

# convert the data (2000 numbers) in to type float
flData = np.empty((0, length))
for i in range(length):
    numData = float(data[i])
    flData = np.append(flData, numData)
    
newflData = flData[0:100] # slice data for high pass filter

# calculate the filter wieghts for low frequency
weightLow = np.empty((0, length)) # array for weight data
for n in range( L ):
    if (n != M/2):
        weight_l = (np.sin(2*np.pi*ft_low*(n - M/2) ) ) / (np.pi*(n - M/2) )
        weightLow = np.append(weightLow, weight_l)
    else:
        weight_l = 2*ft_low
        weightLow = np.append(weightLow, weight_l)
        
low_convolved = np.convolve(flData, weightLow) # convolve float data with weight data

# calculate the filter weights for high frequency
weightHigh = np.empty((0, length)) # array for weight data
for n in range( L ):
    if (n != M/2):
        weight_h = -(np.sin(2*np.pi*ft_high*(n - M/2)))/(np.pi*(n - M/2))
        weightHigh = np.append(weightHigh, weight_h)
    else:
        weight_h = 1 - 2*ft_high
        weightHigh = np.append(weightHigh, weight_h)
        
high_convolved = np.convolve(flData, weightHigh) # convolve float data with weight data
high_convolved2 = high_convolved[0:100] # slice convolved data for plotting highpass filter

# plotting data and range for lowpass filter
t1 = np.arange(0, 2, 1/1000)
x1 = np.cos(2*np.pi*4*t1)
name1a = "Original Signal"
name2a = "4 Hz Signal"
name3a = "Application of Lowpass Filter"
plt.subplot(3, 1, 1)
plt.plot(flData)
plt.title(name1a)
plt.subplot(3,1,2)
plt.plot(x1)
plt.title(name2a)
plt.subplot(3,1,3)
plt.plot(low_convolved)
plt.title(name3a)
plt.tight_layout() #prevents overlapping of title and plot
plt.show()

# plotting data and range for highpass filter
t2 = np.arange(0, 1, 1/100)
t3 = np.arange(0,100)
x2 = np.cos(2*np.pi*330*t2) # 330 Hz signal
name1b = "Original Signal"
name2b = "330 Hz Signal"
name3b = "Application of Highpass Filter"
plt.subplot(3, 1, 1)
plt.plot(t3, newflData)
plt.title(name1b)
plt.subplot(3,1,2)
plt.plot(t3, x2)
plt.title(name2b)
plt.subplot(3,1,3)
plt.plot(t3, high_convolved2)
plt.title(name3b)
plt.tight_layout() #prevents overlapping of title and plot
plt.show()