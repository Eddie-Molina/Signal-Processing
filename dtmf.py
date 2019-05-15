"""
    Eddie Molina
    CSE 3313-001
    Spring 2018
    HW-05
"""
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.signal import freqz


####### Variables #########
fs = 8000   # sampling rate
L = 64      # filter length

#filter bank of bandpass filters
fb1 = 697
fb2 = 770
fb3 = 852
fb4 = 941
fb5 = 1209
fb6 = 1336
fb7 = 1447

""" 
Read in csv file and extract
data. Also count the how many numbers
in file and store in variable length.
"""
with open('tones.csv', 'r') as csvfile:
    readData = csv.reader(csvfile, delimiter = ',')
    for i in readData:
        data = i
        length = len(i)

"""
convert data to float and
store in array
"""
fldata = np.empty((0, length))
for i in range(length):
    numdata = float(data[i])
    fldata = np.append(fldata, numdata)

# initialize arrays for filter coefficients
h_n1 = np.empty((0, L))
h_n2 = np.empty((0, L))
h_n3 = np.empty((0, L))
h_n4 = np.empty((0, L))
h_n5 = np.empty((0, L))
h_n6 = np.empty((0, L))
h_n7 = np.empty((0, L))

# calculate filter coeffients
for n in range(L):
    h1 = (2/L)*np.cos((2*np.pi*fb1*n)/(fs))
    h_n1 = np.append(h_n1, h1)
    h2 = (2/L)*np.cos((2*np.pi*fb2*n)/(fs))
    h_n2 = np.append(h_n2, h2)
    h3 = (2/L)*np.cos((2*np.pi*fb3*n)/(fs))
    h_n3 = np.append(h_n3, h3)
    h4 = (2/L)*np.cos((2*np.pi*fb4*n)/(fs))
    h_n4 = np.append(h_n4, h4)
    h5 = (2/L)*np.cos((2*np.pi*fb5*n)/(fs))
    h_n5 = np.append(h_n5, h5)
    h6 = (2/L)*np.cos((2*np.pi*fb6*n)/(fs))
    h_n6 = np.append(h_n6, h6)
    h7 = (2/L)*np.cos((2*np.pi*fb7*n)/(fs))
    h_n7 = np.append(h_n7, h7)

# initialize arrays for convolution performed in while loop    
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
y7 = []
numbers = [] #array to store characters    

i = 0
while i < length:
    fldata1 = fldata[i:i + 4000] #slice data
    y1 = np.convolve(h_n1, fldata1)
    y2 = np.convolve(h_n2, fldata1)
    y3 = np.convolve(h_n3, fldata1)
    y4 = np.convolve(h_n4, fldata1)
    y5 = np.convolve(h_n5, fldata1)
    y6 = np.convolve(h_n6, fldata1)
    y7 = np.convolve(h_n7, fldata1)
      
    # frequencies present in a particular tone      
    f1 = np.mean(y1**2)
    f2 = np.mean(y2**2)
    f3 = np.mean(y3**2)
    f4 = np.mean(y4**2)
    f5 = np.mean(y5**2)
    f6 = np.mean(y6**2)
    f7 = np.mean(y7**2)
    
    # determine which of the filters has the highest value in row frequency
    row = 0
    if f1 > row:
        row = f1
    if f2 > row:
        row = f2
    if f3 > row:
        row = f3
    if f4 > row:
        row = f4    
    # determine which of the filters has the highest value in column frequency   
    column = 0
    if f5 > column:
        column = f5
    if f6 > column:
        column = f6
    if f7 > column:
        column = f7
    # determine which character is equivalent to the row freq and column freq   
    if f1 == row and f5 == column:
        numbers = np.append(numbers,'1')
    if f1 == row and f6 == column:
        numbers = np.append(numbers, '2')
    if f1 == row and f7 == column:
        numbers = np.append(numbers, '3')
    if f2 == row and f5 == column:
        numbers = np.append(numbers, '4')    
    if f2 == row and f6 == column:
        numbers = np.append(numbers, '5')
    if f2 == row and f7 == column:
        numbers = np.append(numbers, '6')
    if f3 == row and f5 == column:
        numbers = np.append(numbers, '7')
    if f3 == row and f6 == column:
        numbers = np.append(numbers, '8')
    if f3 == row and f7 == column:
        numbers = np.append(numbers, '9')
    if f4 == row and f5 == column:
        numbers = np.append(numbers, '*')
    if f4 == row and f6 == column:
        numbers = np.append(numbers, '0')
    if f4 == row and f7 == column:
        numbers = np.append(numbers, '#')                            
    i += 4000

# print the numbers in file
length1 = len(numbers)
for i in range(length1):
    print(numbers[i], end = '')
    
# apply window to look at the frequency response
x1, y1 = freqz(h_n1, 1)  

# plot filter response for the filter coefficients produced using 697 Hz
plt.figure()
plt.plot(x1, abs(y1))
plt.show()




