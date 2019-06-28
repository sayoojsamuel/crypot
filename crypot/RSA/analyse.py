from Crypto.Util.number import *
from gmpy2 import *
from Crypto.PublicKey import RSA

#TODO:
class RSA:
    def __init__(self,n=None,e=None,c=None):
        self.n = n
        self.e = e
        self.c = c
        self.attendance={}

    def update(self,n=None,e=None,c=None,d=None,p=None,q=None,dp=None,dq=None,phi=None):
        self.n = n
        self.e = e
        self.c = c
        self.d = d
        self.p = p
        self.q = q
        self.dp = dp 
        self.dq = dq
        self.phi = phi
    

    def autofill(self):
        
        pass

    def recover_d(self):
        if self.p or self.q:
            self.autofill()
        self.d = invert(self.e,self.phi)
    
    def recover_primes(self):
        if self.d and self.e:
            _key = RSA.construct((n,e,d))
            self.p = _key.p
            self.q = _key.q
            assert(self.n == self.p*self.q)
            self.phi = (self.p-1)*(self.q)
        else:
            raise Exception("Require d and e to recover the primes")
    
    def factorise(self):
        if self.n:
            _factor_attack(self.n) #TODO: Complete it as soon as possible, Its just a wrapper to call the factor attacks
        pass
    
    def _factor_attack(n):
        pass

            

        
    
class RSAanalyse:
    def __init__(self,RSA):
        self.attendance={}
        
    
    def analyse(self):
        nsize = size(n)
        esize = size(e)


        
        

        
    

    
    
