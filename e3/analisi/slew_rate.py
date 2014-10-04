#! -*- encoding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat

# s = salita, d = discesa

# SALITA
data_s = np.genfromtxt(open("../dati/scope_0.csv"), delimiter=",", skip_header=2)
cut = np.genfromtxt(open("../dati/scope_12.csv"), delimiter=",", skip_header=2)

t_s = data_s[:,0]
v1_s = data_s[:,1] / 2.0
v2_s = data_s[:,2] / 2.0

dts = (t_s[1] - t_s[0]) / 2.0
dv = 0.05

start_ts = min(t_s)
end_ts = max(t_s)
min_s = np.mean(v2_s[t_s < 0])
max_s = np.mean(v2_s[t_s > 0.0000188])

s10 = ufloat(min_s + (max_s - min_s) * 0.1, dv)
s90 = ufloat(min_s + (max_s - min_s) * 0.9, dv)
t10s = 0
t90s = 0

last_v = None
last_t = None
for current_v, t in zip(v2_s[(0 < t_s) & (t_s < 0.0000188)], t_s[(0 < t_s) & (t_s < 0.0000188)]):
    if last_v is None:
        pass
    elif last_v < s10 and current_v > s10:
        t10s = ufloat((last_t + t) / 2.0, dts)
    elif last_v < s90 and current_v > s90:
        t90s = ufloat((last_t + t) / 2.0, dts)
    
    last_v = current_v
    last_t = t

#print(t10, t90, s10, s90)
srs = (s90 - s10) / (t90s - t10s)
print("SALITA: {} V/s oppure {} V/μs".format(srs, srs/1e6))

# DISCESA
data_d = np.genfromtxt(open("../dati/scope_6.csv"), delimiter=",", skip_header=2)

t_d = data_d[:,0]
v1_d = data_d[:,1] / 2.0
v2_d = data_d[:,2] / 2.0

dtd = (t_d[1] - t_d[0]) / 2.0

start_td = min(t_d)
end_td = max(t_d)
min_d = np.mean(v2_d[t_d < 1.9999e-3])
max_d = np.mean(v2_d[t_d > 2.0285e-3])

d10 = ufloat(min_d + (max_d - min_d) * 0.1, dv)
d90 = ufloat(min_d + (max_d - min_d) * 0.9, dv)
t10d = 0
t90d = 0

last_v = None
last_t = None
for current_v, t in zip(v2_d[(1.9999e-3 < t_d) & (t_d < 2.0285e-3)], t_d[(1.9999e-3 < t_d) & (t_d < 2.0285e-3)]):
    if last_v is None:
        pass
    elif last_v > d10 and current_v < d10:
        t10d = ufloat((last_t + t) / 2.0, dtd)
    elif last_v > d90 and current_v < d90:
        t90d = ufloat((last_t + t) / 2.0, dtd)
    
    last_v = current_v
    last_t = t

#print(t10, t90, s10, s90)
srd = (d90 - d10) / (t90d - t10d)
print("DISCESA: {} V/s oppure {} V/μs".format(srd, srd/1e6))

# PLOTS
# salita
f1 = plt.figure()
ax1 = f1.add_subplot(111)

p2 = ax1.errorbar(x=t_s, y=v2_s)
ax1.plot([start_ts, end_ts], [max_s, max_s])
ax1.plot([start_ts, end_ts], [min_s, min_s])
ax1.plot([start_ts, end_ts], [s10.nominal_value, s10.nominal_value])
ax1.plot([start_ts, end_ts], [s90.nominal_value, s90.nominal_value])
ax1.plot([t10s.nominal_value, t10s.nominal_value], [min_s, max_s])
ax1.plot([t90s.nominal_value, t90s.nominal_value], [min_s, max_s])

ax1.set_xlim((start_ts, end_ts))

# discesa
f2 = plt.figure()
ax2 = f2.add_subplot(111)

p2 = ax2.errorbar(x=t_d, y=v2_d)
ax2.plot([start_td, end_td], [max_d, max_d])
ax2.plot([start_td, end_td], [min_d, min_d])
ax2.plot([start_td, end_td], [d10.nominal_value, d10.nominal_value])
ax2.plot([start_td, end_td], [d90.nominal_value, d90.nominal_value])
ax2.plot([t10d.nominal_value, t10d.nominal_value], [min_s, max_s])
ax2.plot([t90d.nominal_value, t90d.nominal_value], [min_s, max_s])

ax2.set_xlim((start_td, end_td))

# niceness
f11 = plt.figure(figsize=(6, 5))
ax11 = f11.add_subplot(111)
f11.suptitle("Slew rate")

p4 = ax11.errorbar(x=t_s, y=v1_s, linewidth=2, c="gray")
p3 = ax11.errorbar(x=t_s, y=v2_s, linewidth=2, c="black")
ax11.errorbar([start_ts, end_ts], [s10.nominal_value, s10.nominal_value], c="black", fmt="--")
ax11.errorbar([start_ts, end_ts], [s90.nominal_value, s90.nominal_value], c="black", fmt="--")
ax11.errorbar([t10s.nominal_value, t10s.nominal_value], [-6, s10.nominal_value], c="black", fmt="--")
ax11.errorbar([t90s.nominal_value, t90s.nominal_value], [-6, s90.nominal_value], c="black", fmt="--")

ax11.set_xticklabels(("", "-20", "-10", "0", "10", "20"))
ax11.set_xlim((start_ts, end_ts))
ax11.set_ylim((-6, 6))
ax11.set_xlabel(u"Tempo [μs]")
ax11.set_ylabel("Tensione [V]")
ax11.grid(True)

ax11.legend((p3, p4), ("Ingresso", "Uscita"), loc="upper left")
f11.savefig("../figure/slew_graph1.pdf")

# niceness
f111 = plt.figure(figsize=(6, 5))
ax111 = f111.add_subplot(111)
f111.suptitle("Slew rate")

pin = ax111.errorbar(x=cut[:,0], y=cut[:,1], linewidth=2, c="gray")
pout = ax111.errorbar(x=cut[:,0], y=cut[:,2], linewidth=2, c="black")

ax111.set_xticklabels(("", "-40", "-20", "0", "20", "40"))
ax111.set_xlim((-0.00005, 0.00005))
ax111.set_ylim((-12, 12))
ax111.set_xlabel(u"Tempo [μs]")
ax111.set_ylabel("Tensione [V]")
ax111.grid(True)

ax111.legend((pin, pout), ("Ingresso", "Uscita"), loc="upper left")
f111.savefig("../figure/slew_signal3.pdf")

# mostra
plt.show()
