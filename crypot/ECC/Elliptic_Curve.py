from Crypto.PublicKey import *
from Crypto.Util.number import *
from gmpy2 import *

class Curve(object):
    def __init__(self,p,a,b):
        self._p = p
        self._a = a
        self._b = b

    def p(self):
        return self._p

    def a(self):
        return self._a

    def b(self):
        return self._b


    def contains_point(self,x,y):
        return (y*y - x*x*x - (self._a*x) - self._b) % self._p == 0

class Point(object):
    def __init__(self,curve,x,y,order=None):
        self._curve = curve
        if curve!=None:
            assert(self._curve.contains_point(x,y))
        self._x = x
        self._y = y
        self._order = order
        global INFINITY

    def _add(self,other):
        if other == INFINITY:
            return self
        elif self == INFINITY:
            return other

        if self._x == other._x:
            if self._y == -(self._y):
                return INFINITY
            else:
                return self._double()
        slope = ((other._y - self._y) * inverse(other._x - self._x,self._curve.p())) % self._curve.p() 
        x3 = (pow(slope,2) - self._x - other._x) % self._curve.p()
        y3 = -(self._y + (slope * (x3 - self._x))) % self._curve.p()
        return Point(self._curve,x3,y3)


    def _double(self):
        slope = ((3 * self._x * self._x + self._curve.a()) * inverse(2*self._y, self._curve.p())) % self._curve.p()
        x3 = (pow(slope,2) - self._x - self._x) % self._curve.p()
        y3 = -(self._y + (slope * (x3 - self._x))) % self._curve.p()
        return Point(self._curve,x3,y3)
        
    def _mul(self, n):
        bits = bin(n)[2:][::-1]
        point = self
        res = INFINITY
        for i in bits:
            if i=='1':
                res = res._add(point)
            point = point._double()
        return res

    def x(self):
        return self._x
    def y(self):
        return self._y
    def coord(self):
        return (self._x,self._y)
    
    def mirror_point():
        return Point(self._curve,self._x,-self._y % self._curve._p)
    
    def equal_points(Q):
        if (Q._x == self._x) and (Q._y == self._y) and (Q._curve == self._curve):
            return True
        else:
            return False

 
INFINITY = Point(None,None,None)

if __name__ == "__main__":
    INFINITY = Point(None,None,None)

    p = 889774351128949770355298446172353873
    a = 12345
    b = 67890

    px, py = (238266381988261346751878607720968495, 591153005086204165523829267245014771)
    qx, qy = (341454032985370081366658659122300896, 775807209463167910095539163959068826)

    E = Curve(p,a,b)
    P = Point(E,px,py)
    Q = Point(E,qx,qy)
    P_plus_Q = (323141381196798033512190262227161667, 775010084514487531788273912037060561)
    twelveP = (771157329084582589666569152178346504, 869049850567812139357308211622374273)
    if P._add(Q).coord()==P_plus_Q:
        print "Success"
    if P._mul(12).coord()==twelveP:
        print "Success"

    


