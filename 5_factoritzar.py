import numpy as np
import matplotlib.pyplot as plt
import timeit
import random
from utils import *

test = 545610561620048
print("Factorització en nombres primers de: ",test)
print(factors_primers(test))


def fact_rep():

    i = 0
    llargada = 4
    mides = list()
    temps = list()
    while i < 7:
        n = random.getrandbits(llargada)


        if es_primer(n):
            llargada += llargada//2
            i +=1
            temps_inicial = timeit.default_timer()
            factors_primers(n)
            temps_final = timeit.default_timer()
            temps_invertit = temps_final - temps_inicial
            mides.append(len(str(n)))
            temps.append(temps_invertit)


    plt.plot(mides, temps, '-gD')
    plt.xlabel("Nombre de dígits")
    plt.ylabel("Segons")
    plt.show()

fact_rep()
