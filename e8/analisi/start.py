import matplotlib.pyplot as plt
import numpy as np
import sys

f = plt.figure()
ax = f.add_subplot(111)


data = np.genfromtxt('../dati/scope_4.csv', delimiter=",", skip_header=2)
    
x = data[:,0]
v1 = data[:,1]

signal = v1
transform = np.fft.fft(signal)
freq = np.fft.fftfreq(len(signal), d=0.001)

#p1 = ax.errorbar(x=x, y=v1)
p2 = plt.plot(freq, transform)
plt.grid(True)

plt.show()
