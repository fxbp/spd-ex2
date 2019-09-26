import numpy as np
import matplotlib.pyplot as plt
import timeit
import random


def mcd_euclides(dividend , divisor):
#Calcula el màxim comú divisor de a i b usant l'algorisme d'Euclides
    residu = dividend % divisor
    while residu != 0:
        dividend = divisor
        divisor = residu
        residu = dividend % divisor

    return divisor


def mcd_input():
    dividend = input("entreu un dividend natural positiu: ")
    divisor = input("entreu un divisor natural positiu: ")
    temps_inicial = timeit.default_timer()
    resultat = mcd_euclides(int(dividend), int(divisor))
    temps_final = timeit.default_timer()
    temps_invertit = temps_final - temps_inicial
    print("Dividend: ",dividend)
    print("Divisor: ", divisor)
    print("MCD: ", resultat)
    print(len(dividend))
    print("Temps invertit: %.10f segons" % (temps_invertit))


def mcd_rep():

    i = 0
    llargada = 32
    llargada2 = 24
    mides = list()
    temps = list()
    while i < 15:
        dividend = random.getrandbits(llargada)
        divisor = random.getrandbits(llargada2)
        llargada *=2
        llargada2 *=2
        i +=1
        temps_inicial = timeit.default_timer()
        resultat = mcd_euclides(dividend, divisor)
        temps_final = timeit.default_timer()
        temps_invertit = temps_final - temps_inicial
        mides.append(len(str(dividend)))
        temps.append(temps_invertit)


    plt.plot(mides, temps, '-gD')
    plt.show()


mcd_rep()
