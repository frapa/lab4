import matplotlib.pyplot as plt
import numpy as np
import sys

f = plt.figure(figsize=(5, 5))
ax = f.add_subplot(111)

data = np.genfromtxt(open("../dati/scope_1.csv"), delimiter=",", skip_header=2)
    
x = data[:,0]
v1 = data[:,1]

p1 = ax.errorbar(x=x, y=v1, c="black", lw=2)

plt.title("Dente di sega")
plt.ylabel("Tensione [V]")
plt.xlabel("Tempo [s]")
plt.xlim((-0.455, 0.305))
plt.ylim((-4.5, 0.5))
plt.grid(True)
plt.subplots_adjust(left=0.12, bottom=0.12, right=0.95)

plt.show()
f.savefig("../figure/dds.pdf")
