from math import *
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat, unumpy

data_low = np.genfromtxt(open("../dati/guadagno_bassa_freq.csv"), delimiter=",", skip_header=1)

freq_low = data_low[:,0]
va_low = unumpy.uarray(data_low[:,1] / 2.0, data_low[:,3])
vout_low = unumpy.uarray(data_low[:,2] / 2.0, data_low[:,4])

G_low = 1001 * vout_low / va_low

data_high = np.genfromtxt(open("../dati/guadagno_alta_freq.csv"), delimiter=",", skip_header=1)

freq_high = data_high[:,0] * 1000
va_high = unumpy.uarray(data_high[:,1] / 2.0, data_high[:,3])
vout_high = unumpy.uarray(data_high[:,2] / 2.0, data_high[:,4])

G_high = vout_high / va_high


f1 = plt.figure()
ax1 = f1.add_subplot(111)
ax1.set_xscale('log')
ax1.set_yscale('log')

p1 = ax1.errorbar(x=freq_low, y=unumpy.nominal_values(G_low))
p2 = ax1.errorbar(x=freq_high, y=unumpy.nominal_values(G_high))

ax1.set_xlim((1, 1e6))


plt.show()
