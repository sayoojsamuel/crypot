from Crypto.Util.number import *
from gmpy2 import *


'''
    :param a - generator
    :param b - yeild beta
    :param p - group of order p
'''

def pollardRho(alpha,beta,p):
    '''
    '''
    def calc_ab(x,a,b):
        # group 2
        if(x%3 == 0):
            x = x*x %p
            a = a*2 % (p-1)
            b = b*2 % (p-1)
        # group 3
        elif(x%3 == 1):
            x = x*alpha % p
            a = (a+1) % (p-1)
        # group 1
        elif(x%3==2):
            x = x*beta % p
            b = (b+1) % (p-1)
        return (x,a,b)
    
    order = ( p-1 )
    x=1
    a,b = 0,0
    X=1
    A,B = 0,0
    i = 1
    #for i in range(order):
    while(i<p-1):
        # Tortise - hop once
        x,a,b = calc_ab(x,a,b)
        # Hare    - hop twice 
        X,A,B = calc_ab(X,A,B)
        X,A,B = calc_ab(X,A,B)
        print i,x,a,b,X,A,B
        if(x==X): 
            print "x==X"
            break     # Completed total iteration over grp
        i+=1
    #return a,b,A,B
    try:
        assert(gcd(a-A,p)==1)
    except:
        print "No Result, gcd = ",gcd(a-A,p)
        return None
    secret = ((a-A)*inverse(B-b,p)) % (p)
    return secret


if __name__=="__main__":
    g = 2
    y = 5
    p = 1019

    secret = pollardRho(g,y,p)
    print secret,secret==10







