from math import log
from uncertainties import ufloat

R10 = ufloat(1e4, 500)
R20 = ufloat(2e4, 1000)
C = ufloat(1e-7, 2e-8)

F10 = 1/(-2*R10*C*log(1/3.0))
F20 = 1/(-2*R20*C*log(1/3.0))

print(F10, F20)