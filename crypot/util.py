"""
The ba3ic blocks of required
""" 

def xor(*m):
    """
    xor(string1, string2[, string3...]) -> string
    :param *m: strings 
    :return: string with xor of all the strings, cut to the smallest input
    """
    from operator import xor
    xoredList =  [reduce(xor,map(ord,x),0) for x in zip(*m)]
    return ''.join(map(chr,xoredList))

def s2n(s):
    """
    s2n("secret") -> 126879297332596
    String to Number
    """
    return int(s.encode('hex'),16) if len(s) else 0
    
