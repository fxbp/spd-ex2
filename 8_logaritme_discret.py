from utils import potencia_modular_eficient

def logaritme_discret(n, base, argument):
    k = -1
    res = -1
    while(res != argument):
        k +=1
        res = potencia_modular_eficient(base, k, n)


    return k


def log_discret_input():
    n = int(input("entreu la n de Z/n: "))
    base = int(input("Entreu la base del logaritme discret: "))
    argument = int(input("Entreu l'argument del logaritme discret: "))

    k = logaritme_discret(n,base,argument)

    print("Logaritme discret en base {} de {} = {} (mod {})".format(base,argument,k,n))


log_discret_input()

#n = 23, b=3, a=12 --> k=4
