from Crypto.Util.number import *
from Crypto.PublicKey import *
import random
from hashlib import *
import hmac


def brute(g,a,p):
	x=1
	while(True):
    		m = long_to_bytes((pow(g,x,p)))
		message = "This is a really cool message"
		mac = hmac.new(m,message,sha1).hexdigest()
		if mac==a:
        		return x
        	else:
        		x+=1

def get_generator(p):         
    p = IntegerModRing(p).multiplicative_generator()
    return p   

def find_order(g,p):
	l = divisors(p-1)
	l=l[1:-1]
	for i in l:
		m=(p-1)//i
		if(pow(g,m,p)==1):
			return m
	return 0
def Alice(B):
	x=2434549512124126637919504123142926982619919
	key = long_to_bytes(pow(B,x,p))
	message = "This is a really cool message"
	mac = hmac.new(key,message,sha1).hexdigest()
	return mac

def Forger(B,x,p):
	key = long_to_bytes(pow(B,x,p))
	message = "This is a really cool message"
	mac = hmac.new(key,message,sha1).hexdigest()
	return mac

def Small_Subgroup_Attack(g,order,p):
	fac = list(factor((p-1)//order))
	for i in range(len(fac)):
		fac[i]=mul(fac[i])
	r_list=[]
	x_list=[]
	#_g = get_generator(p)
	_g = 10
	for i in range(0,len(fac)):
		r = fac[i] 
		h = pow(_g,(p-1)//r,p)
		mac= Alice(h)
		x = brute(h,mac,p)
		r_list.append(r)
		x_list.append(x)
		#if mul(r_list)>order:
		#	break
		s = CRT(x_list,r_list)
		if Forger(123,s,p)==Alice(123):
			break
	return s

		
			
		
				

if __name__=="__main__":
   
# 
#	p = getPrime(256L)
#    g = getRandomInteger(128L)
#    print "-------Calculating Order-------"
#    order = find_order(g,p)
#    if order ==0:
#        print "Wrong Order"
#        exit()
#    print "-------Order Calculated-------"
#    x = random.randint(1,order-1)
#    print g
#    print order
#    print p
#

	p = 7199773997391911030609999317773941274322764333428698921736339643928346453700085358802973900485592910475480089726140708102474957429903531369589969318716771
	g = 4942287684376779101837168233946209616471075701752378896980441495206001478347759519898815588364181508885080635716588152235483592408355096320095820910320456
	q = 236234353446506858198510045061214171961   
	print Small_Subgroup_Attack(g,q,p)


	
