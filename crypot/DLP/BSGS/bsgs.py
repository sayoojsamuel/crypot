from gmpy2 import *

def bsgs(g,a,p):
    ## Shanks algorithm to find x
    ## pow(g,x,p)=a
    m = iroot(p-1,2)[0]
    l = [pow(g,i,p) for i in range(m)]
    x = pow(g,-m,p)
    for j in range(m):
        c = (a * pow(x,j,p)) % p
        if c in l:
            return j*m + l.index(c)



