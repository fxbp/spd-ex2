import numpy as np
import matplotlib.pyplot as plt
import timeit
import random
import math
from utils import bezoud



def bezoud_input():
    dividend = input("entreu un dividend natural positiu: ")
    divisor = input("entreu un divisor natural positiu: ")
    temps_inicial = timeit.default_timer()
    mcd, r, s = bezoud(int(dividend), int(divisor))
    temps_final = timeit.default_timer()
    temps_invertit = temps_final - temps_inicial
    print("Dividend: ",dividend)
    print("Divisor: ", divisor)
    print("MCD: mcd = {}, r = {}, s={} ".format(mcd,r,s))
    print("Comprovacio {} = {} * {} + {}*{}".format(mcd,r,dividend,s,divisor))

    print("Temps invertit: %.10f segons" % (temps_invertit))




bezoud_input()
