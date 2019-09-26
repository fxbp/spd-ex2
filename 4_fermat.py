import random

def fermat_primalitat(n):

    for i in range(1,n):
        b = i
        if pow(b,n-1) % n != 1:
            return False
    return True

print(fermat_primalitat(9491))
