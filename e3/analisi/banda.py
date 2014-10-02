from math import *
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat, unumpy

# 20 dB
data20 = np.genfromtxt(open("../dati/banda_20.csv"), delimiter=",", skip_header=1)

freq20 = data20[:,0]
vout20 = unumpy.uarray(data20[:,1] / 2.0, 10*np.ones(len(freq20)))
phase20 = data20[:,2]
dphase20 = data20[:,3]

vin20 = ufloat(50, 0.5)
db20 = 20.0 * unumpy.log10(vout20/vin20)
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
m3db40 =  db40[0].nominal_value - 3.0

p3db40 = None
for f1, db1, f2, db2 in zip(freq40[:-1], db40[:-1], freq40[1:], db40[1:]):
    if db1 > m3db40 and db2 < m3db40:
        p3db40 = f1 + (f2 - f1) * (m3db40 - db1) / (db2 - db1)
print(p3db40)

f1 = plt.figure()
ax1 = f1.add_subplot(111)
ax1.set_xscale('log')

p2 = ax1.errorbar(x=freq20, y=unumpy.nominal_values(db20))
ax1.plot([10, 1e6], [m3db, m3db])
ax1.plot([p3db.nominal_value, p3db.nominal_value], [1, 24])

ax1.set_xlim((10, 1e6))

f2 = plt.figure()
ax2 = f2.add_subplot(111)
ax2.set_xscale('log')

p2 = ax2.errorbar(x=freq40, y=unumpy.nominal_values(db40))
ax2.plot([10, 1e6], [m3db40, m3db40])
ax2.plot([p3db40.nominal_value, p3db40.nominal_value], [1, 40])
ax2.plot([p3db40.nominal_value], [m3db40], "o")

ax2.set_xlim((10, 1e6))

plt.show()
