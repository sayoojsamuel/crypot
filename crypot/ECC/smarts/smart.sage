from sage.all import *
p = 730750818665451459112596905638433048232067471723
E = EllipticCurve(GF(p), [
        425706413842211054102700238164133538302169176474,
        203362936548826936673264444982866339953265530166
])
 
g = E(125270202464411072778547771568975423382990845665, 440970603958123875213441435758390311809187352362)
v = E(296939092187233862778999244256460019221379646447, 650021996391906816753000782344884033217784284632)
 
def hensel_lift(curve, p, point):
    A, B = map(long, (E.a4(), E.a6()))
    x, y = map(long, point.xy())
 
    fr = y**2 - (x**3 + A*x + B)
    t = (- fr / p) % p 
    t *= inverse_mod(2 * y, p)  # (y**2)' = 2 * y
    t %= p
    new_y = y + p * t
    return x, new_y
 
# lift points
x1, y1 = hensel_lift(E, p, g)
x2, y2 = hensel_lift(E, p, v)
 
# calculate new A, B (actually, they will be the same here)
mod = p ** 2
 
A2 = y2**2 - y1**2 - (x2**3 - x1**3)
A2 = A2 * inverse_mod(x2 - x1, mod)
A2 %= mod
 
B2 = y1**2 - x1**3 - A2 * x1
B2 %= mod
 
# new curve
E2 = EllipticCurve(IntegerModRing(p**2), [A2, B2])
 
# calculate dlog
g2s = (p - 1) * E2(x1, y1)
v2s = (p - 1) * E2(x2, y2)
 
x1s, y1s = map(long, g2s.xy())
x2s, y2s = map(long, v2s.xy())
 
dx1 = (x1s - x1) / p
dx2 = (y1s - y1) / p
dy1 = (x2s - x2)
dy2 = (y2s - y2)
 
m = dy1 * inverse_mod(dx1, p) * dx2 * inverse_mod(dy2, p)
m %= p
 
print m
