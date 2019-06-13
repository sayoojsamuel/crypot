#!/usr/bin/env sage

def smarts_attack(E,P,Q):
	p = E.base().cardinality()
	A = E.a4()
	B = E.a6()
	xP = P[0] 
	yP = P[1]
	xQ = Q[0]
	yQ = Q[1]

	assert E.order() == p

	Qp = Qp(p, 2)
	Ep = EllipticCurve(Qp, [0, 0, 0, A, B])

	yPp = sqrt(Qp(xP) ** 3 + Qp(A) * Qp(xP) + Qp(B))
	Pp = Ep(Qp(xP), (-yPp, yPp)[yPp[0] == yP])

	yQp = sqrt(Qp(xQ) ** 3 + Qp(A) * Qp(xQ) + Qp(B))
	Qp = Ep(Qp(xQ), (-yQp, yQp)[yQp[0] == yQ])
	lQ = Ep.formal_group().log()(- (p * Qp)[0] // (p * Qp)[1]) / p
	lP = Ep.formal_group().log()(- (p * Pp)[0] // (p * Pp)[1]) / p

	e = lQ / lP
	assert e[0] * E(xP, yP) == E(xQ, yQ)
	return e[0]
