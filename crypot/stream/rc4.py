from itertools import cycle

def key_schedule(key):
    s = range(256)
    key_bytes = cycle(ord(x) for x in key)

    j = 0
    for i in xrange(256):
        j = (j+ s[i] + next(key_bytes)) % 256
        s[i],s[j] = s[j], s[i]

    return s

def psuedorandom_generator(s):
    j = 0
    for i in cycle(range(256)):
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]

        j = (s[i] + s[j]) % 256
        yeild s[k]

