#https://grocid.net/2017/09/16/finding-close-prime-factorizations/
def close_factor(n, b):

    # approximate phi
    phi_approx = n - 2 * gmpy.sqrt(n) + 1

    # create a look-up table
    look_up = {}
    z = 1
    for i in range(0, b + 1):
        look_up[z] = i
        z = (z * 2) % n

    # check the table
    mu = gmpy.invert(pow(2, phi_approx, n), n)
    fac = pow(2, b, n)
    j = 0

    while True:
        mu = (mu * fac) % n
        j += b
        if mu in look_up:
            phi = phi_approx + (look_up[mu] - j)
            break
        if j > b * b:
            return

    m = n - phi + 1
    roots = (m - gmpy.sqrt(m ** 2 - 4 * n)) / 2, \
            (m + gmpy.sqrt(m ** 2 - 4 * n)) / 2

    return roots

n = 2462649746477364143454082050368305440553491900304388646893610847386194301369924385009730987303651345060031438478297733694036327257723431468649220444397635127530301992505638291521092898714917678389314956983918603221732358628680256253537449204312287724750669208856634711056863315465220853759428826555838536733
b = 10000000

close_factor(n, b)
