import matplotlib.pyplot as plt
import numpy as np
import sys

f = plt.figure(figsize=(6, 5))
ax = f.add_subplot(111)

data = np.genfromtxt("../dati/scope_1.csv", delimiter=",", skip_header=2)

x = data[:,0]
v1 = data[:,1]
v2 = data[:,2]

p1 = ax.errorbar(x=v1, y=v2, c="black", lw=2)

plt.xlim((0, 2))

plt.xlabel("Input [V]")
plt.ylabel("Output [V]")
plt.title("Isteresi della porta NOT")
plt.grid(True)

plt.annotate("Salita", xy=(1.13, 1.5), xytext=(1.3, 2), fontsize=16,
                  bbox=dict(boxstyle="round4", fc="w"),
    arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=-0.2", fc="w"))
    
plt.annotate("Discesa", xy=(1, 1), xytext=(0.5, 0.5), fontsize=16,
                  bbox=dict(boxstyle="round4", fc="w"),
    arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=-0.2", fc="w"))

plt.show()
if len(sys.argv) > 1:
    f.savefig("../figure/ist.pdf")
