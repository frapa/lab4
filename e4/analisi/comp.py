import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt("../dati/img5.csv", delimiter=",", skip_header=2)

t = data[:,0] * 1000
vin = data[:,1]
vout = data[:,2]

#plt.rc('text', usetex=True)

f = plt.figure(figsize=(8, 5))
ax = f.add_subplot(111)
ax2 = ax.twinx()

pin = ax.plot(t, vin, c="black", linewidth=1.5)
pout = ax2.plot(t, vout, c="#666666",  linewidth=1.5)

ax2.spines['right'].set_color('#666666')
ax2.yaxis.label.set_color('#666666')
ax2.tick_params(axis='y', colors='#666666')

ax.set_title("Comparatore")
ax.set_xlabel("Tempo [ms]")
ax.set_ylabel(r"$V_{in}$ [V]")
ax2.set_ylabel(r"$V_{out}$ [V]")

ax.set_xlim((-2.5, 2.5))
ax2.set_ylim((-4, 16))
ax2.set_xlim((-2.5, 2.5))
ax.set_ylim((-0.2, 0.8))
ax.grid(True)

plt.show()
f.savefig("../figure/comp_graph.pdf")
