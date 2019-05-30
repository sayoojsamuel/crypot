from Crypto.Util.number import *
from Crypto.PublicKey import *

def Pollard_rho(EC,P,Q):

    a = 1
    b = 0
    x = P
    order = EC.order()
    
    def ab(x,a,b):
        y_coord = int(x[1])
    	if y_coord%3 == 1:
            a = a
            b = (b + 1) % order
            x = x + Q
        
        elif y_coord%3 == 2:
            x = 2*x
            a = (2 * a) % order
            b = (2 * b) % order
        elif y_coord%3 == 0:
            x = x + P
            a = (a +1)% order
            b = b
        return x,a,b

    A = a
    B = b
    X = x

    while(1):
        x,a,b = ab(x,a,b)

        X,A,B = ab(X,A,B)
        X,A,B = ab(X,A,B)

        if X==x:
            break

    _B = (B - b)%order
    _A = (a - A)%order


    res = (_A * inverse(_B,order)) % order
    return res/GCD(_B,order)

if __name__=="__main__":
    p = 11731241281
    a = 32
    b = 12
    E = EllipticCurve(GF(p), [a,b])
    P = E(3888567059 ,1277411479)
    for i in range(10):
	x = randint(0,12515)
        Q = x*P
        if Pollard_rho(E,P,Q) == x:
            print "Success"
        else:
            print "failed"
   


