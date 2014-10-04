# -*- encoding: utf-8 -* 
import numpy as np
import matplotlib.pyplot as plt

from uncertainties import ufloat as uf
R = uf(10000, 500)
R1 = uf(50000, 2500)
G = R/R1
print(G)

data = np.genfromtxt("../dati/scope_1.csv", delimiter=",", skip_header=2)

t = data[:,0] * 1000
vout = data[:,1] / 2.0 - 0.1
vin = data[:,2] / 2.0

f = plt.figure(figsize=(8, 5))
ax = f.add_subplot(111)
f.suptitle("Sommatore pesato di tensioni")

v1 = ax.errorbar([-2.5, 2.5], [1, 1], linewidth=2, fmt="-", c="gray")
v2 = ax.errorbar(t, vin, linewidth=2, fmt="--", c="black")
vo = ax.errorbar(t, vout, linewidth=2, fmt="-", c="black")
adc = ax.errorbar([-2.5, 2.5], [-0.2, -0.2], fmt="-", c="black")

ax.set_xlabel("Tempo [ms]")
ax.set_ylabel("Tensione [V]")

ax.set_xlim((-2.5, 2.5))
ax.set_ylim((-0.7, 1.2))

ax.text(x=2.55, y=-0.25, s="-0.2 V")

ax.grid(True)

ax.legend((v1, v2, vo), ("$V_1$", "$V_2$", "$V_{out}$"))

plt.show()
f.savefig("../figure/graph.pdf")
