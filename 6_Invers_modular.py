from utils import bezoud
import numpy as np
import matplotlib.pyplot as plt
import timeit
import random

def invers_modular(k,n):
#retorna k^-1 (mod n) si existeix l'invers modular de k a (mod n)
    mcd, r, s = bezoud(k,n)
    if mcd != 1:
        False, k
    else:
        return True, (r % n)




def invers_input():
    k = int(input("entreu un enter al que voleu buscar invers (mod n) "))
    n = int(input("entreu el modul: "))
    res, invers = invers_modular(k,n)
    if not res:
        print("No hi ha invers modular per {} a (mod {})".format(k,n))
    else:
        print("Invers modular de  {} a (mod {})".format(k,n))
        print("{}^(-1) (mod {}) = {}".format(k,n,invers))

def invers_rep():

    i = 0
    llargada = 4
    llargada2 = 6
    mides = list()
    temps = list()
    while i < 15:
        dividend = random.getrandbits(llargada)
        divisor = random.getrandbits(llargada2)
        llargada *=2
        llargada2 *=2
        i +=1
        temps_inicial = timeit.default_timer()
        resultat = invers_modular(dividend, divisor)
        temps_final = timeit.default_timer()
        temps_invertit = temps_final - temps_inicial
        mides.append(len(str(dividend)))
        temps.append(temps_invertit)

    plt.plot(mides, temps, '-gD')
    plt.xlabel("Nombre de dígits")
    plt.ylabel("Segons")
    plt.show()


invers_rep()

#invers_input()
