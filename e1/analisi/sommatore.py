# coding: utf-8
from uncertainties import ufloat as uf
R = uf(3900, 3900*0.05)
R1 = uf(50000, 2500)
G = R/R1
G
