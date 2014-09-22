# coding: utf-8
from math import *
# Scrivo incertezze
dR = 3900 * 0.05 # 5%
dV = 0.005 # incertezza risoluzione generatore corrente continua 3.90 volt (forse arriva anche al millesimo, ma esageriamo!)
R = 3900
V = 3.9
I = V/R
I
dI = sqrt((dV/R)**2 + (V/R**2*dR)**2)
dI
# Ora provo col paccetto
from uncertainties
from uncertainties import ufloat
Vi = ufloat(V, dV)
Ri = ufloat(R, dR)
Ii = Vi/Ri
Ii
# Perfetto!
