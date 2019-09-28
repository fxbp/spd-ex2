from utils import bezoud

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


invers_input()
