from uncertainties import ufloat, unumpy
import numpy as np

# CALCOLO DI V_OFFSET
# Iniziamo con i dati
v_out = ufloat(-0.97, 0.03)
R1 = ufloat(10, 0.5)
R2 = ufloat(10000, 500)

v_offset = v_out / (1 + R2/R1)
print('v_offset = {}'.format(v_offset))

v_out_trimmer = unumpy.uarray((0.003, 0.01), (0.003, 0.01))
v_offset_trimmer = v_out_trimmer / (1 + R2/R1)
print('v_offset_trimmer = {}'.format(v_offset_trimmer))

# CALCOLO DELLE CORRENTI
v_out_ip1 = unumpy.uarray((2.95, 2.81, 2.55), (0.005, 0.005, 0.005))
Ri = ufloat(100000, 5000)
Ip1 = v_out_ip1 / (Ri + R2/R1*Ri - R2)
media = sum(unumpy.nominal_values(Ip1))/3
s_media = np.std(unumpy.nominal_values(Ip1))
print('Ip- = {}, media = {}+/-{}'.format(Ip1, media, s_media))

v_out_ip2 = ufloat(-2.88, 0.005)
Ip2 = (v_out_ip2 + R2*Ip1) / ((1 + R2/R1)*Ri)
print('Ip+ = {}'.format(Ip2))

# CORREZIONE V_OFFSET
v_offset = (v_out + R2*Ip1) / (1 + R2/R1)
print('v_offset = {}'.format(v_offset))

v_offset_trimmer = (v_out_trimmer[0] + R2*Ip1) / (1 + R2/R1)
print('v_offset_trimmer = {}'.format(v_offset_trimmer))
