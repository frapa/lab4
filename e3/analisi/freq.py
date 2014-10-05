from math import *
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat, unumpy

data_low = np.genfromtxt(open("../dati/guadagno_bassa_freq.csv"), delimiter=",", skip_header=1)

freq_low = data_low[:,0]
va_low = unumpy.uarray(data_low[:,1] / 2.0, data_low[:,3])
vout_low = unumpy.uarray(data_low[:,2] / 2.0, data_low[:,4])

G_low = 1001 * vout_low / va_low

data_high = np.genfromtxt(open("../dati/guadagno_alta_freq_sum.csv"), delimiter=",", skip_header=1)

freq_high = data_high[:,0] * 1000
va_high = unumpy.uarray(data_high[:,1] / 2.0, data_high[:,3])
vout_high = unumpy.uarray(data_high[:,2] / 2.0, data_high[:,4])

G_high = vout_high / va_high


f1 = plt.figure()
ax1 = f1.add_subplot(111)
ax1.set_xscale('log')
ax1.set_yscale('log')

p1 = ax1.errorbar(x=freq_low, y=unumpy.nominal_values(G_low), fmt="o", c="black")
p2 = ax1.errorbar(x=freq_high, y=unumpy.nominal_values(G_high), fmt="o", c="gray")

ax1.set_title("Guadagno di un opamp in funzione della frequenza")
ax1.set_xlabel("Frequenza [Hz]")
ax1.set_ylabel("Amplificazione")
ax1.set_xlim((1, 3e6))
ax1.set_ylim((1e-1, 1e6))
ax1.grid(True)

ax2 = ax1.twinx()
ax2.set_yticks([0.0, 0.143, 0.286, 0.428, 0.571, 0.714, 0.857, 1.0])
ax2.set_yticklabels(("-20", "0", "20", "40", "60", "80", "100", "120", "140"))
ax2.set_ylabel("Amplificazione [dB]")

ax2.legend((p1, p2), ("Bassa freq.", "Alta freq."))

plt.show()
f1.savefig("../figure/A_vs_freq.pdf")