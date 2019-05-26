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
    s2n(string) -> int

    String to Number
    """
    return int(s.encode('hex'),16) if len(s) else 0

def n2s(n):
    """
    n2s(int) -> string

    Number to String
    """
    s = hex(n)[2:]
    if len(s) %2 != 0:
        s = "0" +s
    return s.decode('hex')

def s2b(s):
    """
    String to binary
    """
    return bin(s2n(s))[2:]

def b2s(b):
    """
    Binary to String
    """
    return n2s(int(b,2))

def blen(n):
    """
    Length of bin(n)
    """
    return len(bin(m)[2:])

def ror(s,shift):
    """
    Rotate Right the string s by a count of 'shift'

    'shift' supports negetive numbers for opposite rotate
    """
    split = len(s) - (shift % len(s))
    return s[split:]+s[:split]

def rol(s,shift):
    """
    Rotate Left the string s by a count of 'shift'

    'shift' supports negetive numbers for opposite rotate
    """
    split =  (shift % len(s))
    return s[split:]+s[:split]
