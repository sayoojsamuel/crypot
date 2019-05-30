from Crypto.PublicKey import *
from Crypto.Util.number import *
from gmpy2 import *
import primefac
import random


def factor(n):
    x = list( primefac.primefac(n))
    fac = sorted(list(set(list((i, x.count(i)) for i in x))))
    return fac

class NoSol(Error):
    """No Solution in the small subgroup"""
    pass


def bsgs(g,a,p):
    m = isqrt(p-1)
    l = [pow(g,i,p) for i in range(m)]
    x = pow(g,-m,p)
    for j in range(m):
        c = (a * pow(x,j,p)) % p
        if c in set(l):
            return j*m + l.index(c)
    raise NoSol("No solution in subgroup")

def brute(g,a,p):
        x=1
	while(True):
            if pow(g,x,p)==a:
                return x
            else:
                x+=1


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

def ph(g,a,p):
    n = p-1
    factors = factor(n)
    a_list=[]
    n_list=[]
    for i,j in factors:
        s = 0
	g0 = pow(g,n/i,p)
	for rnd in range(1,j+1):
	    a0 = pow(a * pow(inverse(g,p),s,p) , n/(pow(i,rnd,p)),p)
	    x0 = brute(g0,a0,p)
	    s+= x0 * pow(i,rnd-1,p)
    	a_list.append(s)
	n_list.append(pow(i,j))
    return int(CRT(a_list,n_list)) 
    
def get_generator(p):
    p = IntegerModRing(p).multiplicative_generator()
    return p


def generate_groups():
    p=1
    for i in range(100):
        x = getPrime(10)
        p = p*x
    for i in range(1000000):
        if isPrime(p+1):
            return p+1,get_generator(p+1)
        else:
            p=p*2

if __name__ == '__main__':
   
    f = open('group_list').read()
    f = f.replace('\n','')
    f = eval(f)
    for i in f:
        p = i[0]
        g= i[1]
        x = random.randrange(0,1241241249102412512059712059102957019275010257019275)
        y = pow(g,x,p)
        assert(ph(g,y,p)==x)
        print "Success"

    
    














