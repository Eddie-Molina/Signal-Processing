"""
    Eddie Molina
    CSE 3313-001
    Spring 2018
    HW-05
"""
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.signal import freqz
fc = 7500   #cut-off frequency
L = 101     #filter length
M = L - 1   #filter filter order

data, samplerate = sf.read('P_9_2.wav') #read in .wav file
f_t = fc/samplerate #normalized transition frequency

# calculate the filter weights for low frequency
h_n = np.empty((0, L))
for n in range(L):
    if (n != M/2):
        h = (np.sin(2*np.pi*f_t*(n - (M/2))) / (np.pi*(n - (M/2))))
        h_n = np.append(h_n, h)
    else:
        h = 2*f_t
        h_n = np.append(h_n, h)

# calculate the filter weights for hamming window
hammingData = np.empty((0, L))
for i in range(L):
    w_n = 0.54 - 0.46*np.cos((2*np.pi*i)/M)
    hammingData = np.append(hammingData, w_n)

h_hat = h_n * hammingData # perform element wise multiplication

# apply window to look at the frequency response
x1, y1 = freqz(h_n, 1)  
x2, y2 = freqz(h_hat, 1)

# plot filter response for the filter coefficients
plt.figure() 
plt.plot(x1, abs(y1))  
plt.plot(x2, abs(y2)) 
plt.show() 

convData = np.convolve(data, h_hat) # convolve data with h hat
sf.write('cleanMusic.wav', convData, samplerate) # produce a file with noise removed