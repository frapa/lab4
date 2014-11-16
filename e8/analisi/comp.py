# -*- encoding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import sys

f = plt.figure(figsize=(6, 4.5))
ax = f.add_subplot()

data = np.genfromtxt("../dati/scope_15.csv", delimiter=",", skip_header=2)
data2 = np.genfromtxt("../dati/scope_16.csv", delimiter=",", skip_header=2)
data3 = np.genfromtxt("../dati/scope_17.csv", delimiter=",", skip_header=2)

x = data[:,0] * 1000
v1 = data[:,1]

x2 = data2[:,0] * 1000
v2 = data2[:,1]

x3 = data3[:,0] * 1000
v3 = data3[:,1]

plt.plot(x, v1, label="Sovracompensato", lw=2, c="#bbbbbb")
plt.plot(x2, v2, label="Sottocompensato", lw=2, c="#666666")
plt.plot(x3, v3, label="Compensato", c="black", lw=2)

plt.title("Compensazione sonda")
plt.xlabel("Tempo [s]")
plt.ylabel("Tensione [V]")

plt.xlim((-0.6, 0.4))
plt.ylim((-1, 3.5))
plt.grid(True)

plt.subplots_adjust(left=0.13, bottom=0.13, right=0.95, top=0.92)
plt.legend(fontsize=13, loc="lower right")

plt.show()
if len(sys.argv) > 1:
    f.savefig("../figure/comp.pdf")
