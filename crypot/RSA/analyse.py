from Crypto.Util.number import *
from gmpy2 import *
from Crypto.PublicKey import *

#TODO:
class RSA:
    def __init__(self,n=None,e=None,c=None):
        self.n = n
        self.e = e
        self.c = c

    def update(self,d=None,p=None,q=None):
        self.d = d
        self.p = p
        self.q = q

    
    
