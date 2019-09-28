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


## El test de primalitat de fermat comprova que tots els numeros de 1..n-1, la seva potencia_modular sigui 1 (mod n)
print(fermat_primalitat(561))
## El test de carmichael també utilitza la propietat b^(n-1) congruent 1 (mod n) pero només per aquelles b que siguin coprimers amb b
print(carmichael(561))
