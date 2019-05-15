"""
    Eddie Molina
    CSE 3313-001
    Spring 2018
    HW-06
"""
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

#read in data from .wav file
data, samplefile = sf.read("P_9_2.wav")

#apply fft to data in file
data_fft = []
data_fft = np.fft.fft( data )

#plot data with noise
plt.figure()
plt.plot( abs(data_fft) )
plt.show()

length = len(data)
midpoint = length/2
offset = 10000

for i in range(length):
    if i == (midpoint - offset):    #start at begining of noise
        for j in range(offset * 2): #range from begining of noise to end of noise
            data_fft[i] = 0         #zero out noise
            i = i + 1
 
#apply inverse fft to data           
data_ffti = []
data_ffti = np.fft.ifft(data_fft)

#create clean .wav file
sf.write("cleanMusic.wav", data_ffti.real, samplefile)

#plot clean data
plt.figure()
plt.plot( abs(data_fft) )
plt.show()