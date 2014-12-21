import matplotlib.pyplot as plt
import numpy as np
import sys

f = plt.figure(figsize=(12, 5))
ax1 = f.add_subplot(131)
ax2 = f.add_subplot(132)
ax3 = f.add_subplot(133)

data = np.genfromtxt("../dati/sinusoide100_pro")
    
x1 = data[:,0] * 1000 - 25000
v1 = data[:,1]

data = np.genfromtxt("../dati/sinusoide1000_pro")
    
x2 = data[:,0] * 1000 - 21500
v2 = data[:,1]

data = np.genfromtxt("../dati/sinusoide10000_10000_pro")
    
x3 = data[:,0] - 37.1
v3 = data[:,1]

p1 = ax1.errorbar(x=x1, y=v1, c="black", lw=2)
p1 = ax2.errorbar(x=x2, y=v2, c="black", lw=2)
p1 = ax3.errorbar(x=x3, y=v3, c="black", lw=2)

ax1.set_xlim((0, 30))
ax1.set_xlabel("Tempo [ms]")
ax1.set_ylabel("Tensione [V]")
ax1.set_title("100 Hz")
ax1.grid(True)

ax2.set_xlim((0, 3))
ax2.set_ylim((-1, 6))
ax2.set_xlabel("Tempo [ms]")
ax2.set_title("1 kHz")
ax2.grid(True)

ax3.set_xlim((0, 10))
ax3.set_xlabel("Tempo [s]")
ax3.set_title("10 kHz")
ax3.grid(True)

plt.subplots_adjust(left=0.06, bottom=0.12, right=0.98)

plt.show()
if len(sys.argv) > 1:
    f.savefig("../figure/camp.pdf")
