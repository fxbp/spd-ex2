import math


def mcd_euclides(dividend , divisor):
#Calcula el màxim comú divisor de a i b usant l'algorisme d'Euclides
    residu = dividend % divisor
    while residu != 0:
        dividend = divisor
        divisor = residu
        residu = dividend % divisor

    return divisor

def factors_primers(nombre):
    llista_fp = []
    if nombre >= 2:
        d = 2
        while d <= math.sqrt(nombre):
            if nombre % d == 0:
                llista_fp.append(d)
                nombre = nombre / d
            else:
                d = d+1

        llista_fp.append(int(nombre))

    return llista_fp

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

def potencia_modular_eficient(base, expo, p):
# p>1
# retorna (base^expo) mod
    if expo == 0:
        return 1
    elif base == 0:
        return 0
    else:
        base_to_exp_div2 = potencia_modular_eficient(base, expo//2, p)
        if expo % 2 == 0 :
            return (base_to_exp_div2 * base_to_exp_div2) % p
        else:
            return (base_to_exp_div2 * base_to_exp_div2* base) % p
