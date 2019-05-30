
def bsgs(P,Q):
    n = isqrt(P.order())
    l = []
    for i in range(n):
        x = Q-(i*n*P)
        l.append(x)
    for i in range(n):
        y = i*P 
        if y in l:
           return i + l.index(y)*n 
             
        



