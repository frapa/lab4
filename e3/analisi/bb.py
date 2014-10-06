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

# 20 dB
data20 = np.genfromtxt(open("../dati/banda_20.csv"), delimiter=",", skip_header=1)

freq20 = data20[:,0]
vout20 = unumpy.uarray(data20[:,1] / 2.0, 10*np.ones(len(freq20)))
phase20 = data20[:,2]
dphase20 = data20[:,3]

vin20 = ufloat(50, 0.5)
db20 = 20.0 * unumpy.log10(vout20/vin20)
G20 = vout20/vin20
m3db = db20[0].nominal_value - 3.0


p3db = None
for f1, db1, f2, db2 in zip(freq20[:-1], db20[:-1], freq20[1:], db20[1:]):
    if db1 > m3db and db2 < m3db:
        p3db = f1 + (f2 - f1) * (m3db - db1) / (db2 - db1)

print(p3db)

# 40 dB
data40 = np.genfromtxt(open("../dati/banda_40.csv"), delimiter=",", skip_header=1)

freq40 = data40[:,0]
vout40 = unumpy.uarray(data40[:,1] / 2.0, data40[:,3]) * 1000
phase40 = data40[:,2]
dphase40 = data40[:,4]

vin40 = ufloat(50, 0.5)
db40 = 20.0 * unumpy.log10(vout40/vin40)
G40 = vout40/vin40
m3db40 =  db40[0].nominal_value - 3.0

p3db40 = None
for f1, db1, f2, db2 in zip(freq40[:-1], db40[:-1], freq40[1:], db40[1:]):
    if db1 > m3db40 and db2 < m3db40:
        p3db40 = f1 + (f2 - f1) * (m3db40 - db1) / (db2 - db1)
print(p3db40)

#f1.subplots_adjust(right=0.95, left=0.07, bottom=0.15, top=0.9)


f1 = plt.figure()
ax1 = f1.add_subplot(111)
ax1.set_xscale('log')
ax1.set_yscale('log')

p1 = ax1.errorbar(x=freq_low, y=unumpy.nominal_values(G_low), yerr=unumpy.std_devs(G_low), fmt="o", c="black")
p2 = ax1.errorbar(x=freq_high, y=unumpy.nominal_values(G_high), yerr=unumpy.std_devs(G_high), fmt="o", c="gray")
p3 = ax1.errorbar(x=freq20, y=unumpy.nominal_values(G20), c="black", linewidth=2)
p4 = ax1.errorbar(x=freq40, y=unumpy.nominal_values(G40), c="gray", linewidth=2)

ax1.set_title("Guadagno dell'opamp e banda passante")
ax1.set_xlabel("Frequenza [Hz]")
ax1.set_ylabel("Amplificazione")
ax1.set_xlim((1, 3e6))
ax1.set_ylim((1e-1, 1e6))
ax1.grid(True)

ax2 = ax1.twinx()
ax2.set_yticks([0.0, 0.143, 0.286, 0.428, 0.571, 0.714, 0.857, 1.0])
ax2.set_yticklabels(("-20", "0", "20", "40", "60", "80", "100", "120", "140"))
ax2.set_ylabel("Amplificazione [dB]")

ax2.legend((p1, p2, p3, p4), ("Bassa freq.", "Alta freq.", "20 dB", "40 dB"))

plt.show()
f1.savefig("../figure/gabp.pdf")
