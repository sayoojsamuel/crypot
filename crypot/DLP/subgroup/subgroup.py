#! /bin/env python

'''
This following code is based on article https://toadstyle.org/cryptopals/57.txt
which solves Cryptopas challenge 57
'''

from random import randint
import hmac
import hashlib
from Crypto.Util.number import *
from gmpy2 import *

def chinese_remainder(n, a):
        sum = 0
        prod = reduce(lambda a, b: a*b, n)
        for n_i, a_i in zip(n, a):
                p = prod / n_i
                sum += a_i * inverse(p, n_i) * p
        return sum % prod

'''


# need a function to find the order of the element
## use a Legrange Theorem


# need a function to find the generator of the group
## use sage function

# need a function to find an element with given order q
## use g^ (p-1)/q
'''

# Modulus p
# almost generator g
# q is a factor of p-1
# j in (p-1)/q

p = 7199773997391911030609999317773941274322764333428698921736339643928346453700085358802973900485592910475480089726140708102474957429903531369589969318716771
g = 4565356397095740655436854503483826832136106141639563487732438195343690437606117828318042418238184896212352329118608100083187535033402010599512641674644143
q = 236234353446506858198510045061214171961
j = 30477252323177606811760882179058908038824640750610513771646768011063128035873508507547741559514324673960576895059570
# factor of j: 2 * 3^2 * 5 * 109 * 7963 * 8539 * 20641 * 38833 * 39341 * 46337 * 51977 * 54319 * 57529 * 96142199 * 46323892554437 * 534232641372537546151 * 80913087354323463709999234471
# small factors of j in j_fact
j_fact = [2, 5, 109, 7963, 8539, 20641, 38833, 39341, 46337, 51977, 54319, 57529]


## Bob's private key, this is kept secret
# x = 4794036293173975643251416226015248613092544601861440077981109632006158953843832906862642817482501602806577791138892865217356990564550406963090464034025732L
# x = 164821959196417457885910463520002557377L # working properly
# x = 189041387527268005872848500233134032125
# x = randint(1,p)
x =     randint(1,q)
def __set_bob_privKey(X):
        global x
        x = X
def __get_bob_privKey():
        return x

## Return element with given order
def element_of_order(g,order,p):
    return pow(g,(p-1)/q,p)

dlist = []
def find_divisors(p):
    dlist = divisors(p)

## Return the order of an element
def find_order(g,p):
    #dlist = divisors(p-1)
    if not dlist: find_divisors(p-1)
    for divisor in dlist[:-1]:
        if pow(g,divisor,p) == 1:
            return divisor      # this is our required order
    return -1 # No divisors found


# step 1 in Pohlig Hellman Algo,
## generated fake Pubkey, and returns the small factor too
## small factor is r
def gen_fake_pubKeys():
        for r in j_fact:
                h=1
                while(h==1):
                        t = randint(1,p-1)
                        h = pow(t,(p-1)//r,p)
                yield (h,r)
# step 2, The value is h is sent to Bob (instead of the publicKey sent to Bob by alice)

# step 3, Bob computes the secret key
## K is the secretKey
K=0
def send_message(h):
        def calc_secret_key(h):
                x = __get_bob_privKey()
                K = pow(h,x,p)
                key = long_to_bytes(K)
                return key
        m = "crazy flamboyant for the rap enjoyment"
        key = calc_secret_key(h)
        t = hmac.new(key, m, hashlib.sha256).hexdigest()
        return (m,t)

# step 4, bruteforce for the value of x mod r
## the value of pow(h,x,p) will be the in the subgroup of r
def brute_x(h,r,message,t):
        for i in range(r):
                K = pow(h,i,p)
                key = long_to_bytes(K)
                mac = hmac.new(key, message, hashlib.sha256).hexdigest()
                if mac==t:
                        # this means that pow(h,i,p) == pow(h,x,p)
                        ## thus i = x mod r
                        return i
        else:
                print "some issue"
                return -1

## the main function:
### mod and rem list for crt function
mod_list = []
rem_list = []
fake_pubKeys = gen_fake_pubKeys()
for pubKey,r in fake_pubKeys:
        message, mac= send_message(pubKey)
        xmodr = brute_x(pubKey, r, message, mac)
        if xmodr<1: continue
        mod_list.append(xmodr)
        rem_list.append(r)
result = crt(mod_list,rem_list)

print "private key of Bob is ", result
print "The actual key is     ", x % q


''' debug main
mod_list = []
rem_list = []
fake_pubKeys = gen_fake_pubKeys()
for pubKey,r in fake_pubKeys:
     print "r: ",r,"\npubKey: ", pubKey
     raw_input()
     message, mac= send_message(pubKey)
     xmodr = brute_x(pubKey, r, message, mac)
     print "Check for xmodr and X mod r:" 
     if xmodr<1: continue
     print "\t\t xmodr: ",xmodr, "and (x % r):", x % r
     print xmodr == x % r
     mod_list.append(xmodr)
     rem_list.append(r)
result = crt(mod_list,rem_list)

print "private key of Bob is ", result
print "The actual key is     ", x % q
'''















