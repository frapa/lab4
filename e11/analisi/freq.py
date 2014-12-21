import matplotlib.pyplot as plt
import numpy as np
import sys

f = plt.figure(figsize=(4.5, 6))
ax = f.add_subplot(211)

data = np.genfromtxt("../dati/ucope_3.csv", delimiter=",", skip_header=2)
data2 = np.genfromtxt("../dati/ucope_4.csv", delimiter=",", skip_header=2)
    
x = data[:,0] * 1000 + 4.4
v1 = data[:,1]
v2 = data[:,2]

x2 = data2[:,0] * 1000 + 4.4
w1 = data2[:,1]
w2 = data2[:,2]

p2 = ax.errorbar(x=x, y=v2, c="gray", lw=2)
p1 = ax.errorbar(x=x, y=v1, c="black", lw=2)

plt.title("Q")
plt.ylabel("Tensione [V]")
plt.xlim((0, 4.3))
plt.ylim((-1, 6))
#plt.legend((p2, p1), ("S", "Q"), loc="lower center")
plt.grid(True)

ax2 = f.add_subplot(212)

q2 = ax2.errorbar(x=x2, y=w2, c="gray", lw=2)
q1 = ax2.errorbar(x=x2, y=w1, c="black", lw=2)

plt.title("Q2")
plt.xlabel("Tempo [ms]")
plt.ylabel("Tensione [V]")
plt.xlim((0, 7.3))
plt.grid(True)

plt.subplots_adjust(top=0.95, bottom=0.1, left=0.15, right=0.97, hspace=0.25)
#plt.legend((q2, q1), ("S", "Q"))

plt.show()
if len(sys.argv) > 1:
    f.savefig("../figure/freq.pdf")
