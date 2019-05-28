#!/usr/bin/env sage

p = 16857450949524777441941817393974784044780411511252189319
A = 16857450949524777441941817393974784044780411507861094535
B = 77986137112576
xP = 5732560139258194764535999929325388041568732716579308775
yP = 14532336890195013837874850588152996214121327870156054248
xQ = 2609506039090139098835068603396546214836589143940493046
yQ = 8637771092812212464887027788957801177574860926032421582

E = EllipticCurve(GF(p), [0, 0, 0, A, B])
assert E.order() == p

Qp = Qp(p, 2)
Ep = EllipticCurve(Qp, [0, 0, 0, A, B])

yPp = sqrt(Qp(xP) ** 3 + Qp(A) * Qp(xP) + Qp(B))
Pp = Ep(Qp(xP), (-yPp, yPp)[yPp[0] == yP])

yQp = sqrt(Qp(xQ) ** 3 + Qp(A) * Qp(xQ) + Qp(B))
Qp = Ep(Qp(xQ), (-yQp, yQp)[yQp[0] == yQ])

print('Pp = {}'.format(Pp))
print('Qp = {}'.format(Qp))
print('-' * 40)

lQ = Ep.formal_group().log()(- (p * Qp)[0] // (p * Qp)[1]) / p
print('log(Q) = {}'.format(lQ))
lP = Ep.formal_group().log()(- (p * Pp)[0] // (p * Pp)[1]) / p
print('log(P) = {}'.format(lP))
print('-' * 40)

e = lQ / lP
print('e = {}'.format(e))

assert e[0] * E(xP, yP) == E(xQ, yQ)

print('\n--> FLAG: {:d}\n'.format(e[0]))
