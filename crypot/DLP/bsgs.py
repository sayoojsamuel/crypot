from operator import itemgetter
from gmpy2 import *

def bsgs(a,b,p):
    ## Shanks algorithm to find the x, 
    ## pow(a,x,p)=b
    # Limitting Variable
    k = int(ceil(sqrt(p-1)))
    ## baby step
    bs=list()
    for j in range(k-1):
        bs.append([j,pow(a,k*j,p)])
    bs.sort(key=lambda x: x[1])
    ## giant step
    gs=list()
    for i in range(k-1):
        gs.append([i,((b%p)*pow(invert(a,p),i,p))%p])
    gs.sort(key=lambda x: x[1])
    #set(bs).intersect(gs)
    flag=0
    for i in range(k-1):
        for j in range(k-1):
            if(bs[i][1]==gs[j][1]):
                print "Catch"
                I = bs[i][0]
                J = gs[j][0]
                flag=1
                break
        if(flag):break
    return (k*J+I)%p
