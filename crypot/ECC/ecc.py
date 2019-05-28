#! /usr/bin/env python

"""
Program to implement Elliptic Curve Operations on a Finite Field
"""
import collections
from Crypto.Util.number import inverse

Point = collections.namedtuple("Point",["x","y"])

class EC_Error(Exception):
    pass

class EC(object):
    def __init__(self, a, b, p):
        try:
            assert( 4*(a**3)+27*(b**2) != 0 )
        except:
            raise EC_Error("Discriminant should not be ZERO")
        self.a = a % p
        self.b = b % p
        self.p = p
        self.zero = Point(0,0)
        self.infinity = Point(None, None)

    def isPoint(self, P):
        lhs = P.y**2 % self.p
        rhs = (P.x**3 + self.a * P.x + self.b) % self.p
        if lhs==rhs: return True
        return False

    def add(self, P , Q):
        """ add two point objects on the curve
        assert if the points lie on the curve first

        if p and q are reflex pairs, then the third point lies on INFINITY
        else use the algorithm
        """
        try:
            assert( self.isPoint(P) and self.isPoint(Q) )
        except:
            EC_Error("Both the Points must be on the Curve")
            pass
        if (P == self.zero): return Q
        if (Q == self.zero): return P

        #reflex pairs
        if (P.x == Q.x) and (P.y != Q.y):
            return self.infinity
        # point doubling, p + p
        if (P == Q):
            slope = (3*(P.x**2)+self.a) * inverse(2 * P.y,self.p) % self.p
        # else p and q are different points
        else:
            slope = (Q.y - P.y) * inverse(Q.x - P.x, self.p) % self.p

        # standard equations are used
        x = ( slope**2 - P.x - Q.x) % self.p
        y = ( slope * (P.x - x) - P.y ) % self.p
        return Point(x,y)

    # Point doubling
    def double(self, P):
        if(P == (self.infinity or self.zero)):
            return P
        return self.add(P,P)

    def mul(self, P, t):
        """ scalar multiply a point with t
        following the double and add algorithm

        Scalar multiply by 2 is same as Point doubling
        assert the mul(Point p, 2) == add(Point p, Point p)
        """
        try:
            assert( self.isPoint(P) )
        except:
            EC_Error("The point p must be on the Curve")
            pass

        res = Point(0,0)
        addend = P
        bits = t
        while bits:
            if bits & 1:
                res = self.add(res,addend)
            addend = self.double(addend)
            bits = bits >> 1
        return res


def test():
    p = Point(238266381988261346751878607720968495, 591153005086204165523829267245014771)
    q = Point(341454032985370081366658659122300896, 775807209463167910095539163959068826)
    ec = EC(12345,67890,889774351128949770355298446172353873)
    r = ec.add(p,q)
    # addition
    try:
        assert(r == Point(x=323141381196798033512190262227161667L, y=775010084514487531788273912037060561L))
        print "Add Works!!"
    except:
        print "Add does not work!"

    # scalar Multiply
    twelvep = Point(771157329084582589666569152178346504, 869049850567812139357308211622374273)
    pmul12 = ec.mul(p,12)
    try:
        assert( pmul12 == twelvep )
        print "Mul Works!!"
    except:
        print "Mul does not work!"

