# -*- encoding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import sys

f = plt.figure(figsize=(12, 6))
ax = f.add_subplot(121)

data = np.genfromtxt("../dati/scope_4.csv", delimiter=",", skip_header=2)
data2 = np.genfromtxt("../dati/scope_10.csv", delimiter=",", skip_header=2)

x = data[:,0] + 1.7
v1 = data[:,1]

x2 = data2[:,0] * 1000
v2 = data2[:,1]

p1 = ax.errorbar(x=x, y=v1, c="black", lw=2)

plt.title("Accensione del circuito")
plt.xlabel("Tempo [s]")
plt.ylabel("Tensione in uscita [V]")

plt.xlim((0, 2.5))
plt.grid(True)

ax2 = f.add_subplot(122)

p2 = ax2.errorbar(x=x2, y=v2, c="black", lw=2)

plt.title("Output dell'oscillatore")
plt.xlabel(u"Tempo [ms]")
plt.ylabel("Tensione in uscita [V]")

plt.xlim((-1.400, 1.400))
plt.ylim((-7, 7))
plt.grid(True)

plt.subplots_adjust(left=0.08, right=0.95)

plt.show()
if len(sys.argv) > 1:
    f.savefig("../figure/stab.pdf")
