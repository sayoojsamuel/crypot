# r_k is the root of the polynomial mod p
# r_kp1 is the root of the polynomial mod p^2
# f(x) is the function
# f'(x) is the diff of the function
# f(r_k) mod p = 0
# find r_kp1 such that, f(r_kp1) mod p^2 = 0

"""
Script with reference to [Wiki]()https://en.wikipedia.org/wiki/Hensel%27s_lemma#Hensel's_lemma_for_p-adic_numbers)
## Hensel's lifting for p-addic numbers
"""

def hensel_paddic_lift(f,p,r):
    """
    :param f - is the function
    :param p - the modulo p
    :param r - f(r) mod p = 0
    """
    t = Mod((- f(r) / p),p)
    t *= inverse_mod(Integer(diff(f)(r)),p)
    return r+(Integer(t)%p)*p

#F.<x> = PolynomialRing(GF(7))
f = x^2 -2
# 3,4 is a solution
r = 3
p=7
out = hensel_paddic_lift(f,p,r)
assert(out==10)
