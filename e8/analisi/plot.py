import matplotlib.pyplot as plt
import numpy as np
import sys

f = plt.figure()
ax = f.add_subplot(111)

if len(sys.argv) == 2:
    data = np.genfromtxt(open(sys.argv[1]), delimiter=",", skip_header=2)
    
    x = data[:,0]
    v1 = data[:,1]

    p1 = ax.errorbar(x=x, y=v1)
    plt.grid(True)

plt.show()
