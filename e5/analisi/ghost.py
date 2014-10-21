# -*- encoding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import sys

data = np.genfromtxt("../dati/f18.csv", delimiter=",", skip_header=2)
datae = np.genfromtxt("../dati/f19.csv", delimiter=",", skip_header=2)

x = data[:,0]*1000 - 12
v1 = data[:,1]
v2 = data[:,2]

xe = datae[:,0]*1000 - 12
v1e = datae[:,1]
v2e = datae[:,2]

f = plt.figure(figsize=(8, 6))

v_in = plt.errorbar(x=x, y=v1, linewidth=2, c="gray")
v_out = plt.errorbar(x=x, y=v2, linewidth=2, c="black")
v_out1 = plt.errorbar(x=xe, y=v2e, fmt="--", linewidth=1.5, c="black")

plt.xlim((-2, 2))

plt.title("Rettificatore migliorato")
plt.xlabel("Tempo [ms]")
plt.ylabel("Tensione [V]")
plt.grid(True)

plt.legend((v_in, v_out, v_out1), ("Input", "Output $V_o$", "$V_{o1}$"), loc="upper left",
	fontsize=13)

plt.show()

if len(sys.argv) > 1:
    f.savefig("../figure/radd_ott_graph.pdf")