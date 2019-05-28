#!/usr/env sage
from IPython import embed
from gmpy2 import invert
def _pollardRho(EC, P, Q, p):
    """
    Solve elliptic curve log in Q = kP
    """
    order = EC.order()
    def calc_ab(A,a,b):
        """
        Search for S in the three sets based in x coordinate
        """
        if(int(A[0])%3 == 0):
            b = (b+1) % order
            return (A+Q,a,b)
        if(int(A[0])%3 == 1):
            a = a*2 % order
            b = b*2 % order
            return (2*A,a,b)
        if(int(A[0])%3 == 2):
            a = (a+1) % order
            return (A+P,a,b)

    x = P
    a,b = 1,0
    X = P
    A,B = 1,0
    i=1
    while(i<order):
        # Tortise - hop once
        x,a,b = calc_ab(x,a,b)
        # Hare - hot twice
        X,A,B = calc_ab(X,A,B)
        X,A,B = calc_ab(X,A,B)
        #print i,x,a,b,X,A,B
        if(x == X):
            print "Cycle found"
            break
        i+=1
    #embed()
    try:
        assert(gcd(B-b,order)==1)
    except:
        print "try the second method"
        return None
    #print "<debug>", a,b,A,B,p
    secret = ( ((a-A)%order) * inverse_mod(B-b,order) ) % order
    #print "<debug> Secret:", secret
    return secret


def test():
    p = 52561L
    a,b = 16023L, 3038L
    EC = EllipticCurve(GF(p),[a,b])
    px, py = (23733, 39516)
    P = EC((px,py))
    r = 123
    Q = r*P

    _pollardRho(EC, P, Q, p)

def test2():
    p = 55049
    a,b = (38063, 19964)
    EC = EllipticCurve(GF(p),[a,b])
    px,py = (42139,35834)
    P = EC((px,py))
    r = 123
    Q = r*P

    _pollardRho(EC, P ,Q, p)

def test3():
    p = 17
    a,b = 2,2
    EC = EllipticCurve(GF(p),[a,b])
    P = EC((5,1))
    r = 10
    Q = r*P

    _pollardRho(EC, P ,Q, p)


print test3()
embed()

