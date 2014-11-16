# -*- encoding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import sys

f = plt.figure(figsize=(6, 4.5))
ax = f.add_subplot(111)

data = np.genfromtxt("../dati/scope_14.csv", delimiter=",", skip_header=2)

x = data[:,0]
v1 = data[:,1]

p1 = ax.errorbar(x=x, y=v1, c="black", lw=2)

plt.title(u"Instabilità dovuta ai capacitori di disaccoppiamento", fontsize=13)
plt.xlabel("Tempo [s]")
plt.ylabel("Tensione in uscita [V]")

plt.xlim((-0.5, 0.5))
plt.grid(True)

plt.show()
if len(sys.argv) > 1:
    f.savefig("../figure/inststab.pdf")
