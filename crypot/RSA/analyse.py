from Crypto.Util.number import *
from gmpy2 import *
from Crypto.PublicKey import RSA
 

#TODO:
class RSA(object):
    def __init__(self, **kwargs):
        input_set = set(kwargs.keys())
        public_set = set(('n','e'))
        for component, value in kwargs.items():
            setattr(self,component,value)
        private_set = public_set | set(('p','q','d','u'))
    # Set the individual properties 
    @property
    def n(self):
        if not self.n
        return int(self.n)

    @property
    def e(self):
        return int(self.e)

    @property
    def d(self):
        return int(self.d)

    @property
    def p(self):
        return int(self.p)

    @property
    def q(self):
        return int(self.q)

    @property
    def u(self):
        return int(self.u)

    @property
    def c(self):
        return int(self.c)

    @property
    def phi(self):
        if not self.phi
        return int(self.phi)
    
    def has_private(self):
        """ If the RSA private key is available """
        # call to autofill, reconstruct d if p and q are available
        # if hasattr(self,"p") or hasattr(self,"q"):
        #     self.recover_d()
        return hasattr(self, "d")

    def update(self, **kwargs):
        """To update the RSA object with the values. 
        Designed to incorporate additional components.
        """
        for component, value in kwargs.items():
            setattr(self,component,value)
        self.autofill()

    def autofill(self):
        """ To calculate other attributes given sufficient parameters """
        # This is supposed to be a very long function, so stay calm

        # Find the value of n, if p or q
        # Or find the value of P or Q

        if hasattr(self,"n"):
            if hasattr(self,"p") and not hasattr(self,"q"):
                setattr(self,"q", self.n//self.p)
            elif hasattr(self,"q") and not hasattr(self,"p"):
                setattr(self,"p", self.n//self.q)
            elif hasattr(self,"phi"):
                # if phi is given
                sumpq =  - self.phi + self.n + 1
                diffpq = iroot(sumpq**2 - r*self.n,2)[0]
                setattr(self,"p",(sumpq+diffpq)//2)
                setattr(self,"q", self.n//self.p)
            else:
                return
            setattr(self,"phi",(self.p-1)*(self.q-1))
            setattr(self,"d",invert(self.e,self.phi))
        else:
            if hasattr(self,"p") and hasattr(self,"q"):
                setattr(self,"n",self.p * self.q)
                setattr(self,"phi",(self.p-1)*(self.q-1))
                setattr(self,"d",invert(self.e,self.phi))   

        # Call to recover primes if d is given
        self.recover_primes()

        # TODO: Complete the case for gcd(e,phi)!=1    
    
    def recover_d(self):
        if self.p or self.q:
            self.autofill()
        self.d = invert(self.e,self.phi)
    
    def recover_primes(self):
        if hasattr(self,"d") and self.e:
            _key = RSA.construct((n,e,d))
            self.p = _key.p
            self.q = _key.q
            assert(self.n == self.p*self.q)
            self.phi = (self.p-1)*(self.q-1)
        else:
            raise Exception("Require d and e to recover the primes")
    
    def factlass RSAanalyse:
    def __init__(self,RSA):
        self.attendance={}
        
    
    def analyse(self):
        nsize = size(n)
        esize = size(e)


        if slass RSAanalyse:
    def __init__(self,RSA):
        self.attendance={}
        
    
    def analyse(self):
        nsize = size(n)
        esize = size(e)


            lass RSAanalyse:
    def __init__(self,RSA):
        self.attendance={}
        
    
    def analyse(self):
        nsize = size(n)
        esize = size(e)

it as soon as possible, Its just a wrapper to call the factor attacks
        passlass RSAanalyse:
    def __init__(self,RSA):
        self.attendance={}
        
    
    def analyse(self):
        nsize = size(n)
        esize = size(e)


    
    def _factor_attack(n):
        pass

            

        
    
class RSAanalyse:
    def __init__(self,RSA):
        self.attendance={}
        
    
    def analyse(self):
        nsize = size(n)
        esize = size(e)



        
        

        
    

    
    
