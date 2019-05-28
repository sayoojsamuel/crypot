from random import *

from Crypto.Util.number import *
from gmpy2 import *
from primefac import primefac

## Need CRT in the end
## n -> Modulus
## a -> Remainder

class Error(Exception):
    pass

class NoSol(Error):
    """No Solution in the small subgroup"""
    pass

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * inverse(p, n_i) * p
    return sum % prod

def brute(a,b,p):
    i=0
    while(1):
        if b == pow(a,i,p): return i
        i+=1
    raise NoSol("No solution in subgroup")

def bsgs(a,b,p):
    print "Bruteforce is better"


## @input: a,b,p
## satisfy b = a**x %p
## @output: x
def prime_factor(p):
    l = [i for i in primefac(p)]
    plist = {(i,l.count(i)) for i in l}
    return plist

def ph(a,b,p):
    phi = p-1
    plist = prime_factor(phi)
    rem_list = []
    mod_list = []
    for prime,count in plist:
        times = count  # make a copy of count
        prev_b = b
        remainder = 0         # remainder
        beta = pow(b,phi/prime,p)
        alpha  = pow(a,phi/prime,p)
        for time in range(1,count+1):
            x0 = brute(alpha,beta,p)
            ## Save the x0 to find X in
            remainder += pow(prime,time-1)*x0
            # changing prev_beta to beta*alpha ^ -x0
            prev_b = prev_b*(pow(invert(a,p), pow(prime,time-1)*x0,p)) %p
            beta = pow(prev_b,phi/prime**(time+1),p)
        rem_list+= [remainder % (prime**count)]
        mod_list+= [prime**count]
    print rem_list
    print mod_list
    result = chinese_remainder(mod_list,rem_list)
    return result



    # Calculate
if __name__=="__main__":
    # p = [i for i in primefac(getPrime(32)-1)]
    # p = [2, 3, 3, 5, 47, 563, 1327L]
    # isPrime(listprod(p)+1) == True
    #p = 3160237231L
    p = 41
    a = 7
    #x =
    #b = pow(a,x,p)
    b = 12
    #print ph(a,b,p)
    l = eval(open("group_list").read().replace("\n",""))
    xgen = lambda :randrange(1,123412341234312343123412341234)
    #   for p,g in l:
    #
    #       x = xgen()
    #       y = pow(g,x,p)
    #       assert(ph(g,y,p)==x)
    #       print "eureka"

    # challenge psiphi asis
    p = 47651074444584490405053939399816975911403196085671060384332813096388260068847568887111713420759535173198203462503052752247366554104035049112507788566669043L
    ct_modp = 25952837942081155822410724444661278336543518379810628450874227064161765071799266591239950002775200213499375501703000603519421119041103661403523773957091543
    #print ph(ct_modp,2,p)
    q = 7607377412242622502208008530344261472220445322720114346607813589307651499896735848796087087920909584771752975927165597032180844800228552430832610027707189L


