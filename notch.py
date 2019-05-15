"""
    Eddie Molina
    CSE 3313-001
    Spring 2018
    HW-07
"""

import numpy as np
import csv
import matplotlib.pyplot as plt


f = 17
fs = 500 #samples per second
n = 2
w_hat = (2*np.pi*f)/fs
x = []
y = [None]*2
with open("notchData.csv") as csvfile:
    readData = csv.reader(csvfile, delimiter = ',')
    for i in readData:
        x = [float(j) for j in i]       
        length = len(i)

for k in range(100):
    x.append(0)

plt.figure(1)
plt.title("Original Signal")
plt.xlim(-25, 625)
plt.plot( x )
plt.show()


y[0] = x[0]
y[1] = 1.8744*np.cos(w_hat)*y[0] + x[1] - 2*np.cos(w_hat)*x[0]

#difference equation for notch filter
while n < length:
    y.append(1.8744*np.cos(w_hat)*y[n-1] - 0.8783*y[n-2] + x[n] - 2*np.cos(w_hat)*x[n-1] + x[n-2])
    n = n + 1

plt.figure(2)
plt.title("Filtered Signal")
plt.ylim(-2.25, 2.25)
plt.plot( y )
plt.show()

x1 = np.arange(0, (length + 100))
x2 = np.cos(2*np.pi*33*x1/fs) # 33 Hz signal
x3 = np.cos(2*np.pi*10*x1/fs) # 10 Hz signal


plt.figure(3)
plt.title("10Hz + 33Hz Signal")
plt.xlim(-25, 625)
plt.plot( x2 + x3 )
plt.show()    