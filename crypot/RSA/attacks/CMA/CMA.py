
from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import gmpy2

# c1 , c2 are the two ciphertext, e1 , e2 are the two exponents and the common modulus

def attack(c1,c2,e1,e2,n):
    g, a, b=gcdext(e1,e2)
    if a<0:
	c1=pow(inverse(c1,n),a*-1,n)
    else:
	c1=pow(c1,a,n)

    if b<0:
	c2=pow(inverse(c2,n),b*-1,n)
    else:
	c2=pow(c2,b,n)

    ct=(c1*c2)%n

    return long_to_bytes(gmpy2.iroot(ct,g)[0])



























