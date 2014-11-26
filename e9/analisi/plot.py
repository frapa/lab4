import matplotlib.pyplot as plt
import numpy as np
import sys

f = plt.figure()
ax = f.add_subplot(111)

if len(sys.argv) == 2:
    data = np.genfromtxt(open(sys.argv[1]), delimiter=",", skip_header=2)
    
    x = data[:,0]
    v1 = data[:,1]
    v2 = data[:,2]

    p1 = ax.errorbar(x=v1, y=v2)
    #p2 = ax.errorbar(x=x, y=v2)
    plt.grid(True)

plt.show()
