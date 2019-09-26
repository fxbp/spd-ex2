import numpy as np
import matplotlib.pyplot as plt
import timeit
import random
import math

def bezoud(dividend , divisor):
#Calcula el màxim comú divisor de a i b usant l'algorisme d'Euclides
    residu = dividend % divisor
    q = dividend // divisor
    i = 2
    r =[1,0]
    s= [0,1]
    while residu != 0:
        r.append(q*r[i-1]+r[i-2])
        s.append(q*s[i-1]+s[i-2])
        dividend = divisor
        divisor = residu
        residu = dividend % divisor
        q = dividend // divisor
        i+=1
    sRes = s[i-1]
    rRes = r[i-1]
    if (i-1)%2==0:
        sRes *=-1
    else:
        rRes *= -1
    return divisor , rRes, sRes


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
