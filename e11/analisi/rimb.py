import matplotlib.pyplot as plt
import numpy as np
import sys

f = plt.figure(figsize=(5, 7))
ax = f.add_subplot(211)

data = np.genfromtxt("../dati/ucope_0.csv", delimiter=",", skip_header=2)
data2 = np.genfromtxt("../dati/ucope_2.csv", delimiter=",", skip_header=2)
    
x = data[:,0] * 1000
v1 = data[:,1]
v2 = data[:,2]

x2 = data2[:,0] * 1000
w1 = data2[:,1]
w2 = data2[:,2]

p1 = ax.errorbar(x=x, y=v1, c="gray", lw=2)
p2 = ax.errorbar(x=x, y=v2, c="black", lw=2)

plt.title("Interruttore a lamina")
plt.ylabel("Tensione [V]")
plt.xlim((-0.03, 0.22))
plt.ylim((-1, 6))
plt.legend((p2, p1), ("S", "Q"), loc="lower center")
plt.grid(True)

ax2 = f.add_subplot(212)

q1 = ax2.errorbar(x=x2, y=w1, c="gray", lw=2)
q2 = ax2.errorbar(x=x2, y=w2, c="black", lw=2)

plt.title("Interruttore 2")
plt.xlabel("Tempo [ms]")
plt.ylabel("Tensione [V]")
plt.xlim((-0.08, 0.75))
plt.grid(True)

plt.subplots_adjust(top=0.95, bottom=0.08, left=0.12, right=0.97, hspace=0.2)
plt.legend((q2, q1), ("S", "Q"))

plt.show()
if len(sys.argv) > 1:
    f.savefig("../figure/rimb.pdf")
