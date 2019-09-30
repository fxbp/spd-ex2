import numpy as np
import matplotlib.pyplot as plt
import timeit
import random
from utils import *


def fermat_primalitat(n):

    for i in range(1,n):
        b = i
        result = potencia_modular_eficient(b,n-1,n)
        if result != 1:
            return False
    return True



def coprimers(a,b):
    return mcd_euclides(a,b) == 1


def carmichael(n):
    for b in range(1,n):
        if coprimers(b,n):
            if potencia_modular_eficient(b,n-1,n) != 1:
                return False

    factors = factors_primers(n)
    setFactors = set(factors)
    return len(setFactors) == len(factors) and len(factors) >=3


def primer_rep():

    i = 0
    llargada = 4
    mides = list()
    temps = list()
    while i < 5:
        test = random.getrandbits(llargada)
        print(test)
        temps_inicial = timeit.default_timer()
        if fermat_primalitat(test):
            llargada += llargada//2
            i += 1
            temps_final = timeit.default_timer()
            temps_invertit = temps_final - temps_inicial
            mides.append(len(str(test)))
            temps.append(temps_invertit)


    plt.plot(mides,temps, '-gD')
    plt.xlabel("Nombre de dígits")
    plt.ylabel("Segons")
    plt.show()

test = 541
print("Test primalitat Fermat de: ",test)

## El test de primalitat de fermat comprova que tots els numeros de 1..n-1, la seva potencia_modular sigui 1 (mod n)
print(fermat_primalitat(test))
## El test de carmichael també utilitza la propietat b^(n-1) congruent 1 (mod n) pero només per aquelles b que siguin coprimers amb b
print("Test nombre charmicael de: ",test)
print(carmichael(test))

primer_rep()
