# -*- encoding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import sys

data = np.genfromtxt("../dati/f9.csv", delimiter=",", skip_header=2)
datae = np.genfromtxt("../dati/f10.csv", delimiter=",", skip_header=2)

x = data[:,0]*1000
v1 = data[:,1]
v2 = data[:,2]

xe = datae[:,0]*1000
v1e = datae[:,1]
v2e = datae[:,2]

f = plt.figure(figsize=(8, 5))

v_in = plt.errorbar(x=x, y=v1, linewidth=2, c="gray")
v_out = plt.errorbar(x=x, y=v2, linewidth=2, c="black")
#v_out1 = plt.errorbar(x=xe, y=v2e, fmt="--", linewidth=1.5, c="black")

plt.xlim((-2.5, 2.5))

plt.title("Rettificatore di precizione a mezz'onda")
plt.xlabel("Tempo [ms]")
plt.ylabel("Tensione [V]")
plt.grid(True)

plt.legend((v_in, v_out), ("Input", "Output"), loc="lower right")

datae = np.genfromtxt("../dati/f4.csv", delimiter=",", skip_header=2)

fe = plt.figure(figsize=(8, 5))

v_ine = plt.errorbar(x=xe, y=v1e, linewidth=2, c="gray")
v_oute = plt.errorbar(x=xe, y=v2e, linewidth=2, c="black")

plt.xlim((-1.5, 1.5))
plt.title("Uscita dell'operazionale confrontata con l'ingresso")
plt.xlabel("Tempo [ms]")
plt.ylabel("Tensione [V]")
plt.grid(True)

plt.legend((v_ine, v_oute), ("Ingresso", "$V_{o1}$"), loc="lower right")

ferr = plt.figure(figsize=(8, 5))
ax = ferr.add_subplot(211)

v_inerr = plt.errorbar(x=x*1000, y=v1, linewidth=2, c="gray")
v_outerr = plt.errorbar(x=x*1000, y=v2, linewidth=2, c="black")

plt.xlim((-100, 100))
plt.ylim((-0.3, 0.3))
ax.axes.xaxis.set_ticklabels(["", "", "", "", ""])

plt.title("Ritardo")
plt.ylabel("Tensione [V]")
plt.grid(True)

plt.legend((v_inerr, v_outerr), ("Ingresso", "$V_{o}$"), loc="lower right")

ax2 = ferr.add_subplot(212)

v_inerr2 = plt.errorbar(x=x*1000 + 11, y=v1, linewidth=2, c="gray")
v_outerr2 = plt.errorbar(x=xe*1000 + 11, y=v2e, linewidth=2, c="black")

plt.xlim((-100, 100))
#plt.ylim((-16, 2))

plt.xlabel(u"Tempo [$\mu$s]")
plt.ylabel("Tensione [V]")
plt.grid(True)

plt.legend((v_inerr2, v_outerr2), ("Ingresso", "$V_{o1}$"), loc="lower right")
ferr.subplots_adjust(hspace=0.03)

plt.show()

if len(sys.argv) > 1:
    f.savefig("../figure/rett.pdf")
    fe.savefig("../figure/rett_vo1.pdf")
    ferr.savefig("../figure/rett_err.pdf")
