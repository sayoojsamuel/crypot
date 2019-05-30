from Crypto.Util.number import *
import random
from gmpy2 import *
import primefac
def factor(n):
    x = list( primefac.primefac(n))
    fac = sorted(list(set(list((i, x.count(i)) for i in x))))
    return max(fac)[0]

def Pollard_Rho1(alpha,beta,p):
    a = 0
    b = 0
    x = 1
    order = factor(p-1)
    #order = p-1
    def ab(x,a,b):
        if x%3 == 1:
            x = (x*beta)%p
            b = (b + 1)%order
        elif x%3 == 2:
            x = (x*x) % p
            a = (2 * a) % order
            b = (2 * b) % order
        elif x%3 == 0:
            x = (x * alpha)%p
            a = (a +1)% order
            b = b
        return x,a,b

    A = a
    X = x
    B = b

    while(1):

        x,a,b = ab(x,a,b)

        X,A,B = ab(X,A,B)
        X,A,B = ab(X,A,B)

        if X == x:
            break


    _B = (B - b)%order
    _A = (a - A)%order

    res = (_A * inverse(_B,order)) % order
    return res/GCD(_B,order),GCD(_B,order),order 
            

def Pollard_Rho2(alpha,beta,p):
    a = 0
    b = 0
    x = 1
    #order = factor(p-1)
    order = p-1
    def ab(x,a,b):
        if x%3 == 1:
            x = (x*beta)%p
            b = (b + 1)%order
        elif x%3 == 2:
            x = (x*x) % p
            a = (2 * a) % order
            b = (2 * b) % order
        elif x%3 == 0:
            x = (x * alpha)%p
            a = (a +1)% order
            b = b
        return x,a,b

    A = a
    X = x
    B = b

    while(1):

        x,a,b = ab(x,a,b)

        X,A,B = ab(X,A,B)
        X,A,B = ab(X,A,B)

        if X == x:
            break


    _B = (B - b)%order
    _A = (a - A)%order

    res = (_A * inverse(_B,order)) % order
    return res/GCD(_B,order),GCD(_B,order),order

def safe_primes(size):
    while(1):
        p=getPrime(size)
        q = (p-1)/2
        if isPrime(q):
            return p,q



if __name__ == '__main__':

    for i in range(20):
        p = getPrime(30)
        g=2
        x = random.randint(1,12414)
        y = pow(g,x,p)
        res,gd,OR = Pollard_Rho1(g,y,p)
        if pow(g,res,p)==y:
            print "1. Pass",gd,OR
        else:
            print "1. fail",gd,OR
	res,gd,OR = Pollard_Rho2(g,y,p)
        if pow(g,res,p)==y:
            print "2. Pass",gd,OR
        else:
            print "2. fail",gd,OR
	print "---------------------------------------------"
