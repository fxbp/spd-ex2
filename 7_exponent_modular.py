from utils import potencia_modular_eficient
import numpy as np
import matplotlib.pyplot as plt
import timeit
import random



def exp_modular_input():
    n = int(input("entreu la n de Z/n: "))
    base = int(input("Entreu la base: "))
    exponent = int(input("Entreu l'exponent : "))

    k = potencia_modular_eficient(base,exponent,n)

    print("Exponenciacio modular {} de {} = {} (mod {})".format(base,exponent,k,n))


def invers_rep():

    i = 0
    llargada = 4
    llargada2 = 6
    n = 17
    mides = list()
    temps = list()
    while i < 25:
        base = random.getrandbits(llargada)
        exponent = random.getrandbits(llargada2)
        llargada *= 2
        llargada2 +=2
        i +=1
        temps_inicial = timeit.default_timer()
        k = potencia_modular_eficient(base, exponent,n)
        temps_final = timeit.default_timer()
        temps_invertit = temps_final - temps_inicial
        mides.append(len(str(llargada)))
        temps.append(temps_invertit)

    plt.plot(mides, temps, '-gD')
    plt.xlabel("Nombre de dígits")
    plt.ylabel("Segons")
    plt.show()


invers_rep()

#exp_modular_input()
