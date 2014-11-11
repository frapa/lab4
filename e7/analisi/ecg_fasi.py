import matplotlib.pyplot as plt
import numpy as np
import sys

f = plt.figure(figsize=(8, 5))
ax = f.add_subplot(111)

data = np.genfromtxt("../dati/scope_2.csv", delimiter=",", skip_header=2)
    
x = data[:,0]
v1 = data[:,1]

p1 = ax.errorbar(x=x, y=v1, c="black")

plt.title("Fasi del battito cardiaco")
plt.xlabel("Tempo [s]")
plt.ylabel("d.d.p. [V]")
plt.xlim((-0.2, 0.7))
plt.grid(True)

plt.plot((-0.05, -0.05, 0.1, 0.1), (-1.8, -2, -2, -1.8), linewidth=2)
plt.plot((0.1, 0.1, 0.2, 0.2), (-4, -4.2, -4.2, -4), linewidth=2)
plt.plot((0.3, 0.3, 0.5, 0.5), (-1.8, -2, -2, -1.8), linewidth=2)
plt.plot((0.5, 0.5, 0.6, 0.6), (0.8, 1, 1, 0.8), linewidth=2)

plt.text(0.02, -2.5, "P")
plt.text(0.13, -4.7, "QRS")
plt.text(0.39, -2.5, "T")
plt.text(0.54, 1.3, "U")

f.subplots_adjust(left=0.1, right=0.95)

plt.show()

if len(sys.argv) > 1:
    f.savefig("../figure/ecg_fasi.pdf")
