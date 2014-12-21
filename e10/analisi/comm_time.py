import matplotlib.pyplot as plt
import numpy as np
import sys

f = plt.figure(figsize=(4.5, 5))
ax = f.add_subplot(111)

data = np.genfromtxt("../dati/scope_1.csv", delimiter=",", skip_header=2)
    
x = data[:,0] * 1e9
v1 = data[:,1]
v2 = data[:,2]

p1 = ax.errorbar(x=x, y=v1, c="gray", lw=2, label="Input")
p2 = ax.errorbar(x=x, y=v2, c="black", lw=2, label="Output")

plt.title("Tempo di commutazione")
plt.xlabel("Tempo [ns]")
plt.ylabel("Tensione [V]")

plt.xlim((-50, 100))
plt.grid(True)
plt.legend(loc="lower right")
plt.subplots_adjust(bottom=0.12, left=0.15, right=0.93)

plt.show()
if len(sys.argv) > 1:
    f.savefig("../figure/comm_time.pdf")