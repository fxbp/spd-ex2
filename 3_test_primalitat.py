import math
import numpy as np
import matplotlib.pyplot as plt
import timeit
import random

def es_primer(nombre):
# <nombre> >= 0, diu si <nombre> és es primer
    if nombre <2:
        return False
    arrel_de_nombre = math.sqrt(nombre)
    for k in range(2, int(arrel_de_nombre)+1):
        if nombre % k == 0:
            return False
    return True



def primer_rep():

    i = 0
    llargada = 4
    mides = list()
    temps = list()
    while i < 8:
        test = random.getrandbits(llargada)
        print(test)
        temps_inicial = timeit.default_timer()
        if es_primer(test):
            llargada += llargada//2
            i += 1
            temps_final = timeit.default_timer()
            temps_invertit = temps_final - temps_inicial
            mides.append(len(str(test)))
            temps.append(temps_invertit)


    plt.plot(mides,temps, '-gD')
    plt.show()


primer_rep()
