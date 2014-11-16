import matplotlib.pyplot as plt
import numpy as np
import sys

f = plt.figure(figsize=(12, 6))
ax = f.add_subplot(121)

data = np.genfromtxt("../dati/scope_2.csv", delimiter=",", skip_header=2)
data2 = np.genfromtxt("../dati/scope_3.csv", delimiter=",", skip_header=2)

x = data[:,0] * 1000 + 50
v1 = data[:,1]

x2 = data2[:,0] * 1000 - 500
v2 = data2[:,1]

p1 = ax.errorbar(x=x, y=v1, c="black", lw=2)

plt.title("Guadagno complessivo > 1")
plt.xlabel("Tempo [ms]")
plt.ylabel("Tensione in uscita [V]")

plt.xlim((0, 100))
plt.grid(True)

ax2 = f.add_subplot(122)

p2 = ax2.errorbar(x=x2, y=v2, c="black", lw=2)

plt.title("Guadagno complessivo < 1")
plt.xlabel("Tempo [ms]")
plt.ylabel("Tensione in uscita [V]")

plt.xlim((0, 200))
plt.grid(True)

plt.subplots_adjust(left=0.08, right=0.95)

plt.show()
if len(sys.argv) > 1:
    f.savefig("../figure/exp_imp.pdf")
