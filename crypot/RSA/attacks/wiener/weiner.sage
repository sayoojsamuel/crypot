
lst = continued_fraction(Integer(e)/Integer(n))
conv = lst.convergents()
for i in conv:
    k = i.numerator()
    d = int(i.denominator())
    try:
        m = hex(pow(c, d, n))[2:].replace("L","").decode("hex")
        if "inctf" in m:
            print m
    except:
        continue
