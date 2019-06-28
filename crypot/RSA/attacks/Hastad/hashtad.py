
from Crypto.Util.number import *
from Crypto.PublicKey import *

def xgcd(a, b):
    x = [1, 0]
    y = [0, 1]
    sign = 1

    while b:
        q, r = divmod(a, b)
        a, b = b, r
        x[1], x[0] = q*x[1] + x[0], x[1]
        y[1], y[0] = q*y[1] + y[0], y[1]
        sign = -sign

    x = sign * x[0]
    y = -sign * y[0]
    return a, x, y

def CRT(a, m):
    modulus = reduce(lambda a,b: a*b, m)
    multipliers = []
    for m_i in m:
        M = modulus / m_i
        gcd, inverse, y = xgcd(M, m_i)
        multipliers.append(inverse * M % modulus)

    result = 0
    for multi, a_i in zip(multipliers, a):
        result = (result + multi * a_i) % modulus
    return result


def hastad_unpadded(ct_list, mod_list, e):
    """
    Implementing Hastad's Broadcast Attack
    """
    m_expo = crt(ct_list, mod_list)
    if m_expo != -1:
        eth_root = gmpy2.iroot(m_expo, e)
        if eth_root[1] == False:
            print "[+] Cannot calculate e'th root!"
            return -1
        elif eth_root[1] == True:
            return long_to_bytes(eth_root)
    else:
        print "[+] Cannot calculate CRT"
        return -1

