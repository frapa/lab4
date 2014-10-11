import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt("../dati/img9.csv", delimiter=",", skip_header=2)
data_tr = np.genfromtxt("../dati/img10.csv", delimiter=",", skip_header=2)

t = data[:,0] * 1e6
vin = data[:,1] * 1000
vout = data[:,2]

t_tr = data_tr[:,0] * 1e6
vin_tr = data_tr[:,1] * 1000
vout_tr = data_tr[:,2]

f = plt.figure(figsize=(12, 6))
ax = f.add_subplot(221)
ax1 = f.add_subplot(223)
ax2 = f.add_subplot(222)
ax21 = f.add_subplot(224)

f.suptitle("Rumore con e senza trigger")

pin = ax1.plot(t, vin, c="black")
pout = ax.plot(t, vout, c="black")

pin_tr = ax21.plot(t_tr, vin_tr, c="black")
pout_tr = ax2.plot(t_tr, vout_tr, c="black")

#ax.set_title("Comparatore")
ax1.set_xlabel("Tempo [$\mu$s]")
ax.set_ylabel(r"$V_{out}$ [V]")
ax1.set_ylabel(r"$V_{in}$ [mV]")
ax.set_xticklabels([])

ax.set_title("Senza soglia")

ax.set_ylabel(r"$V_{in}$ [V]")
ax21.set_xlabel("Tempo [$\mu$s]")
ax2.set_ylabel(r"$V_{out}$ [V]")
ax21.set_ylabel(r"$V_{in}$ [mV]")
ax2.set_xticklabels([])

ax2.set_title("Con soglia")

ax.set_xlim((-1.5, 2.5))
ax.set_ylim((-4, 16))
ax1.set_xlim((-1.5, 2.5))
ax2.set_ylim((-40, 40))

ax2.set_xlim((-1.5, 2.5))
ax2.set_ylim((-4, 16))
ax21.set_xlim((-1.5, 2.5))
ax21.set_ylim((-70, 20))

ax.grid(True)
ax1.grid(True)
ax2.grid(True)
ax21.grid(True)

f.subplots_adjust(left=0.08, right=0.95, hspace=0)

plt.show()
f.savefig("../figure/trigger_graph.pdf")
