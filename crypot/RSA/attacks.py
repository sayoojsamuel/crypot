# Attack Symmary
from Crypto.Util.number import *
from gmpy2 import *

def wiener(e,n):
    """
    Used when the d is very small, otherwise e is very large
    """
    from attacks.wiener import wiener
    
    d = wiener.crack_rsa(e,n)
    if d == None:
        raise Exception("Not suitable for wieners attack")
    return d
    

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
    
def recover_modulus(encrypt,e=None):
    """
    Used to recover modulus, and e if encryption oracle is given
    """
    from attacks.extractmod import extractmod_eunknown,extractmod_eknown
    if type(encrypt)!=function:
        raise Exception("First argument must be a function to encrypt")
    if e==None:
        n = extractmod_eunknown(encrypt)
    else:
        n = extractmod_eknown(encrypt,e)
    return n

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
    from attacks.CMA import CMA
    try:
        c1, c2, e1, e2, n = parameter_list
    except:
        raise Exception("Give the correct parameter list (c1, c2, e1, e2, n)")

    m = CMA(c1,c2,e1,e2,n)
    print "Message Found: ",m
    return m

def hastad_broadcast(ct_list, mod_list):
    """
    Broadcast same message
    """
    from attacks.Hastad.hashtad import hastad_unpadded
    if len(ct_list)!=len(mod_list):
        if len(ct_list)!=3:
            raise Exception("Incorrect Parameteres, Parameters Required (ct_list,mod_list)")
    m = hastad_unpadded(ct_list,mod_list)
    print "Message Found: ", m
    return m

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




def factordb(n, debug=False):
    """
    Api for factor db call

    """
    import requests
    try:
    	response=requests.get("http://factordb.com/api", params={"query": str(n)}).json()
    	if debug: print response
        fac = response['factors']
    	if response["id"]=='C':
            raise ValueError("Factors for this Composite number is not known!")
    	if not fac: return []
        ml = [[int(prime)]*count for prime,count in fac]
        return [y for x in ml for y in x]
    except Exception as e:
       	raise ValueError(e.msg, e.args)
 

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

