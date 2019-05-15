"""
    Eddie Molina
    CSE 3313-001
    Spring 2018
    HW-09
"""
import numpy as np
from scipy import signal
import soundfile as sf
import glob

song_wavs = glob.glob("song-*.wav")
x, fs = sf.read("testSong.wav")
f, t, Sxx = signal.spectrogram(x, fs=fs, nperseg=int(0.5*fs))

""" 
analyze test song and store the maximum frequency within each segment
of the spectrogram and store it in an array called signature1.
"""
x1 = []
index = 0
signature1 = []
for i in range(len(t)):
    x1 = Sxx[:,i]
    maxValue = 0
    j = 0
    index = 0
    for j in range(len(x1)):
        if x1[j] > maxValue:
            maxValue = x1[j]
            index = j
    signature1.append(f[index])

""" 
analyze each song in the database and retreive the amplitudes
of each frequency/time pair in a song and store it in an array called 
signitureList.
"""
signatureList = []
for songs in range(len(song_wavs)):
    x, fs = sf.read(song_wavs[songs])
    f, t, Sxx = signal.spectrogram(x, fs=fs, nperseg=int(0.5*fs))    
    x1 = []
    index = 0
    signature = []
    for i in range(len(t)):
        x1 = Sxx[:,i]
        maxValue = 0
        j = 0
        index = 0
        for j in range(len(x1)):
            if x1[j] > maxValue:
                maxValue = x1[j]
                index = j
        signature.append(f[index])
    signatureList.append(signature)       

normalizedValue = []
for lst in range(len(signatureList)):
    normalizedValue.append(np.linalg.norm((np.array(signatureList[lst]) - np.array(signature1)), ord = 1))

pair = 0
pairList = []
for pair in range(len(song_wavs)):
    pairList.append(str(normalizedValue[pair]) + " " + song_wavs[pair])

sortedPairList = sorted(pairList)
k = 0
for k in range(len(song_wavs)):
    print(sortedPairList[k], "\n")