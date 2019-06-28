# Attack Symmary
from Crypto.Util.number import *
from gmpy2 import *

def wiener():
    """
    Used when the d is very small, otherwise e is very large
    """
    raise NotImplementedError


def wiener_variant():
    """
    Used when the d is very small, otherwise e is very large
    """
    raise NotImplementedError


def bleichenbacher():
    """
    Used for padding oracle (with PKCS#1 v1.5), returning padding error
    """
    raise NotImplementedError

def coppersmiths(parameter_list):
    """
    Used when e is very small or partial knowledge of d is available
    """
    raise NotImplementedError

def invalidPubExponent(c, p,q,e):
    """
    Used when gcd(e,phi)!=1
    """
    phi = (p-1)*(q-1)
    n = p*q
    _gcd = gcd(e,phi)
    if (_gcd==1):
        raise Exception("This is a valid public key")
    d = invert(e//_gcd,phi)
    c = pow(c,d,n)
    m,check = iroot(c,_gcd)
    if check == True:
        return m
    else:
        print "This may not be a valid m"
        return m
    
def recover_modulus(parameter_list):
    """
    Used to recover modulus, and e if encryption oracle is given
    """
    raise NotImplementedError

def blinding(parameter_list):
    """
    Used to decrypt c, provided with a general decryption oracle.
    Also used for blind signing
    """
    raise NotImplementedError

def paritalKeyRecovery(parameter_list):
    """
    lower d bits, about half size is given
    """
    raise NotImplementedError

def common_modulus(parameter_list):
    """
    Multiple messages with same modulus
    """
    raise NotImplementedError

def hastad_broadcast(parameter_list):
    """
    Broadcast same message
    """
    raise NotImplementedError

def boneh_durfee(parameter_list):
    """
    Boneh Durfee attack
    """
    raise NotImplementedError

def pinhole(para):
    """
    RSA d middle two bit leak, redacted
    """
    raise NotImplementedError

def partialPrimes():
    """
    recover d given CRT components and partial prime
    """
    raise NotImplementedError

def multiprime():
    """
    handle multiprime rsa
    """
    raise NotImplementedError

def chosenplaintext():
    """
    CPA on RSA
    """
    raise NotImplementedError


def yafu():
    """
    API call to yafu
    """
    raise NotImplementedError

def neca():
    """
    API call to neca
    """
    raise NotImplementedError




def factordb(para):
    """
    Api for factor db call
    """
    raise NotImplementedError

def fermat():
    """
    fermat factorisation
    """
    raise NotImplementedError

def pollard():
    """
    pollard p-1 for relatively smooth numbers
    """
    raise NotImplementedError

def mersenne():
    """
    mersenne primes factorisation
    """
    raise NotImplementedError

def londahl():
    """
    Carl Londahl's factorisation for close p and q
    """
    raise NotImplementedError

def qicheg():
    """
    factor for unsage primes
    """
    raise NotImplementedError

def sexy():
    """
    factor for sexy primes
    """
    raise NotImplementedError

