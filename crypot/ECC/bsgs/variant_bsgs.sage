#!/usr/env sage
from gmpy import invert
def _bsgs(EC,P,Q,p):
    """
    For P and Q points on the Curve EC, and follows the equation
    > Q = r * P
    find r using BSGS 
    """

    # limit
    k = int(ceil(sqrt(p-1)))
    #baby step
    bs = list()
    for j in range(k-1):
        bs.append(k*j*P)
# check this sorting
    #bs.sort(key=lambda x: x[1])
    
    #giant step
    gs = list()
    for i in range(k-1):
        gs.append(Q - (i*(-P)))
# check this sorting too
    #gs.sort(key=lambda x: x[1])
    # find the intersection
    flag = 0
    for i in bs :
        if i in gs:
            I, J = bs.index(i), gs.index(i)
            flag = 1
            break
        if(flag): break

    return (k*J+I) % p

def test1():
    p = 889774351128949770355298446172353873
    a = 12345
    b = 67890

    EC = EllipticCurve(GF(p),[a,b])
    px, py = (238266381988261346751878607720968495, 591153005086204165523829267245014771)
    P = EC((px,py))
    r = 1234
    Q = r*P

    assert(_bsgs(EC,P,Q,p) == r)

def test2():
    p = 38791L
    a,b = 12345, 29099
    EC = EllipticCurve(GF(p),[a,b])

    px,py = (22670,38330)
    P = EC((px,py))
    r = 123
    Q = r*P

    print _bsgs(EC, P, Q, p)
    print "BSGS worked!"

print "Testing 2"
test2()
