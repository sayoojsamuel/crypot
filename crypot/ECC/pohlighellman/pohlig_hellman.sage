from Crypto.Util.number import *
from Crypto.PublicKey import *
from sage.all import *

def brute(P,Q):
	i = 0
	while True:
		if P*i == Q:
			return i
    
def Pohlig_hellman(E,P,Q):
	order = P.order()
    	fac = list(factor(order))
	sec = []
	mod = []
    	for i,j in fac:
        	st = Q
		P_prime = (order // (i**j)) * P
		z = 0
		lg = 0
		for k in range(1,j+1):
			st = st - (z*i*pow(i,k-1))*P 
			Q_prime = (order // pow(i,k)) * st 	
			z = P_prime.discrete_log(Q_prime) 
			lg += z*pow(i,k-1)	
		sec.append(lg)
		mod.append(i**j)
		secret = CRT(sec,mod)
		if secret*P == Q:
			break		
	return CRT(sec,mod)		
     			
def Pohlig_hellman2(E,P,Q):
	order = P.order()
    	fac = list(factor(order))
	sec = []
	mod = []
    	for i,j in fac:
		P_prime = (order // (i**j)) * P
		Q_prime = (order // (i**j)) * Q
		lg = P_prime.discrete_log(Q_prime)	
		sec.append(lg)
		mod.append(i**j)
		secret = CRT(sec,mod)
		if secret*P == Q:
			break		
	return CRT(sec,mod)		
     			


def test():
	p = 233970423115425145524320034830162017933
	a = -95051
	b_list = [210,504,727]
	for b in b_list:
	    	ec = EllipticCurve(GF(p),[a,b])
		P = ec.random_point()
		import random
		for i in range(100):
			l = random.randint(1234,1234123412)
			Q = l*P
	    		res = Pohlig_hellman2(ec,P,Q)
	    		print res,res == l

test()
