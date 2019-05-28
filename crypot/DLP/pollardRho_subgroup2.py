from Crypto.Util.number import *
from gmpy2 import *


def pollardRho(alpha,beta,p):
    def calc_ab(x,a,b):
        # group 2
        if(x%3 == 2):
            x = x*x %p
            a = a*2 % order
            b = b*2 % order
        # group 3
        elif(x%3 == 0):
            x = x*alpha % p
            a = (a+1) % order
        # group 1
        elif(x%3==1):
            x = x*beta % p
            b = (b+1) % order
        return (x,a,b)

    order = ( p-1 )/2
    x=alpha*beta
    a,b = 1,1
    X=x
    A,B = 1,1
    i = 1
    #for i in range(order):
    for i in xrange(p):
        # Tortise - hop once
        x,a,b = calc_ab(x,a,b)
        # Hare    - hop twice
        X,A,B = calc_ab(X,A,B)
        X,A,B = calc_ab(X,A,B)
        #print i,x,a,b,X,A,B
        if(x==X):
            print "x==X"
            break     # Completed total iteration over grp
    #return a,b,A,B
    try:
        assert(gcd(a-A,p)==1)
    except:
        print "No Result, gcd = ",gcd(a-A,p)
        return None
    secret = ((a-A)*invert(B-b,order)) % (order)
    try:
        assert(pow(alpha,secret,p) == beta)
        return secret
    except: pass
    return secret + order

def verify(g,h,p,x):
    return pow(g,x,p)==h


if __name__=="__main__":
    g = 2
    y = 228
    p = 383

    secret = pollardRho(g,y,p)
    print secret,secret==110
    M = 424242

    args = [
        (2, 11, 59),
        (2, M, 5041259),
        (5, M, 87993167),
        (2, M, 1726565507),
        (7, M, 24455596799),
        (5, M, 368585361623),
        (11, M, 4520967464159),
        (5, M, 66008980226543),
        (5, M, 676602320278583),
        (2, M, 2075952270932339),
        (7, M, 21441211962585599)
    ]

    for arg in args:
        res = pollardRho(*arg)
        print arg, ': ', res
        print "Validates: ", verify(arg[0], arg[1], arg[2], res)
        print






