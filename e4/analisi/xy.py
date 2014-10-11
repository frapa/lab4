import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt("../dati/f0.csv", delimiter=",", skip_header=2)
#data2 = np.genfromtxt("../dati/f2.csv", delimiter=",", skip_header=2)

t = data[:,0] * 1000
vin = data[:,1]
vout = data[:,2]

#t2 = data2[:,0] * 1000
#vin2 = data2[:,1]
#vout2 = data2[:,2]

f = plt.figure(figsize=(8, 5))
ax = f.add_subplot(111)
#ax2 = ax.twinx()

p1 = ax.plot(vin, vout, c="black", linewidth=1)
#p2 = ax.plot(vin2, vout2, c="black", linewidth=1)
#pout = ax.plot(t, vout, c="black",  linewidth=1)

start = ax.errorbar([-0.0129, -0.0129], [-2, 15], fmt="--", c="black")

ax.set_title("Curva di isteresi")
ax.set_xlabel("$V_{in}$ [V]")
ax.set_ylabel(r"$V_{out}$ [V]")
#ax2.set_ylabel(r"$V_{out}$ [V]")

ax.set_xlim((-0.3, 0.3))
ax.set_ylim((-2, 15))
#ax2.set_xlim((-2.5, 2.5))
#ax2.set_ylim((-0.2, 0.8))
ax.grid(True)

ax.annotate('Ingresso\ndescrescente', xy=(-0.025, 7), xytext=(-0.18, 9),
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.2"))
ax.annotate('Ingresso\ncrescente', xy=(0.01, 7), xytext=(0.08, 5),
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.2"),)

f.subplots_adjust(right=0.95)
plt.legend((start,), ("-12.9 mV",), loc="lower right")

plt.show()
f.savefig("../figure/isteresi.pdf")
