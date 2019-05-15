"""
    Eddie Molina
    CSE-3313
    HW-08
"""
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
file = open("shelvingConfig.txt", "r")
text = file.readlines()
name = text[0].strip()
gain = int(text[1].strip())
f_c = int(text[2].strip())
x, f_s = sf.read(name)
length_x = len(x)
length_n = length_x // 4
f0 = f_s / length_x
x_fft = []
x_fft = np.fft.fft( x )
x_fft = x_fft[0:length_n]
length = len(x_fft)
mu = np.power(10,gain/20)
theta = 2*np.pi*f_c/f_s
gamma = (1 - ( 4 / ( 1 + mu ) ) * np.tan(theta / 2))  / (1 + ( 4 / ( 1 + mu ) ) * np.tan(theta / 2) )
alpha = (1 - gamma) / 2
x1 = np.arange(0, length_n) * f0
plt.figure()
plt.ylim(0, np.max(abs(x_fft) +100) )
plt.plot(x1,abs(x_fft))
plt.show()
u = []
y = []
u.append(alpha * x[0])
y.append(x[0] + (mu - 1) * u[0])
n = 1
while n < length_x:
    u.append(alpha*(x[n] + x[n - 1]) + (gamma * u[n - 1]))
    y.append(x[n] + ((mu - 1)*u[n]))
    n+=1
y_fft = np.fft.fft( y )
new_y_fft = y_fft[0:length_n] 
plt.figure()
plt.ylim(0,np.max(abs(x_fft)+100))
plt.plot(x1,  abs(new_y_fft))
plt.show()    