import matplotlib.pyplot as plt
import numpy as np
import sys

f = plt.figure()
ax = f.add_subplot(111)

data = np.genfromtxt("../dati/scope_2.csv", delimiter=",", skip_header=2)
    
x = data[:,0]
v1 = data[:,1]

p1 = ax.errorbar(x=x, y=v1, c="black")

plt.title("Elettrocardiogramma")
plt.xlabel("Tempo [s]")
plt.ylabel("d.d.p. [V]")
plt.xlim((-2, 2))
plt.grid(True)

f.subplots_adjust(left=0.1, right=0.95)

plt.show()

if len(sys.argv) > 1:
    f.savefig("../figure/ecg.pdf")
