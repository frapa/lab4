import matplotlib.pyplot as plt
import numpy as np
import sys
from math import pi

f = plt.figure(figsize=(6, 4.5))
ax = f.add_subplot(111)

R = 1e4
C = 1e-7
w = np.logspace(1.5, 6, 1000)
G = 20 * np.log10(w/2/pi*R*C / np.sqrt((1 - (w/2/pi*R*C)**2)**2 + (3*w/2/pi*R*C)**2))

plt.plot(w, G, c="black", linewidth=2)

plt.plot([2*pi*0.382/R/C, 2*pi*0.382/R/C], [-50, 0], c="gray", ls="--", lw=1.5, label="Poli")
plt.plot([2*pi*2.618/R/C, 2*pi*2.618/R/C], [-50, 0], c="gray", ls="--", lw=1.5)
plt.plot([2*pi/R/C, 2*pi/R/C], [-60, 0], c="black", ls="--", lw=1.5, label="Massimo")

print(2*pi/R/C)

plt.xscale('log')
plt.xlim((10**1.5, 1e6))
plt.ylim((-50, 0))
plt.grid(True)

plt.title("Comportamento in frequenza del partitore")
plt.xlabel("Frequenza [Hz]")
plt.ylabel("Guadagno [dB]")

plt.legend()

plt.show()

if len(sys.argv) > 1:
    f.savefig("../figure/ctp.pdf")
