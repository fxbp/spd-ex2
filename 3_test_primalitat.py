import math
import numpy as np
import matplotlib.pyplot as plt
import timeit
import random
from utils import es_primer




def primer_rep():

    i = 0
    llargada = 4
    mides = list()
    temps = list()
    while i < 7:
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
    plt.xlabel("Nombre de dígits")
    plt.ylabel("Segons")
    plt.show()

start = timeit.default_timer()
test = 1000000000100011
print("Provant si {} es primer".format(test))
print(es_primer(test))
print(timeit.default_timer()-start)
primer_rep()
