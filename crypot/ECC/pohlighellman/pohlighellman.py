
def pohlighellman(ec,P,Q):
    n = P.order()
    factors = list(factor(n))
    li = []
    modi = []
    for p,e in factors[:-1]:
        P0 = (n//p) * P
        z = []
        for i in range(e):
            multiplier = (n // (p**(i+1)))
            BASE = Q
            for j in range(len(z)):
                BASE -= z[j] * (p**j) * P
            Q0 = multiplier * BASE
            z.append(P0.discrete_log(Q0))
        l0 = 0
        for i in range(e):
            l0 += z[i] * (p**i)
        li.append(l0)
        modi.append(p**e)

    return crt(li,modi)

def test():
    ## Parameters from "Alice Sends Bob a meme"
    p = 108453893951105886914206677306984937223705600011149354906282902016584483568647
    a = 829
    b = 512

    # Curve is y^2 = X^3 + ax^2 + b
    # this is different from the normal curve
    ec = EllipticCurve(GF(p),[0,a,0,b,0])
    P = (88610873236405736097813831550942828314268128800347374801890968111325912062058, 76792255969188554519144464321650537182337412449605253325780015124365585152539)
    Q = (27543889954945113502256551007964501073506795938025836235838339960818915950890, 75922969573987021583641685217441284832467954055295272505357185824478295962572)
    P = ec(P)
    Q = ec(Q)
    l_bound = 84442469965344
    l = pohlighellman(ec,P,Q)
    print l,l==1213123123131

def test2():
    ## Parameters from "Cryptopals Challenge 59"
    p = 233970423115425145524320034830162017933
    a = -95051
    b_list = [210,504,727][-1:]

    ## Curve is y^2 = x^3 + ax + b
    for b in b_list:
        ec = EllipticCurve(GF(p),[a,b])

        P = ec.random_point()
        import random
        for _ in range(100):
            l = random.randint(1234,1234123412)
            Q = l*P
            res = pohlighellman(ec,P,Q)
            print res,res == l

def test3():
    ## Parameters from multiplier 1 hack.lu'18
    param = {   "hacklu":
            ((889774351128949770355298446172353873, 12345, 67890),
            # Generator of Subgroup of prime order 73 bits, 79182553273022138539034276599687 to be excact
            (238266381988261346751878607720968495, 591153005086204165523829267245014771),
            # challenge Q = xP, x random from [0, 79182553273022138539034276599687)
            (341454032985370081366658659122300896, 775807209463167910095539163959068826)
            )
        }

    (p, a, b), (px, py), (qx, qy) = param["hacklu"]
    E = EllipticCurve(GF(p), [a, b])
    P = E((px, py))
    Q = E((qx, qy))
    print pohlighellman(E,P,Q)


test()
test2()
#test3()
