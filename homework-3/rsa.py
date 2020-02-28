#!/usr/bin/python2
import os
import json
import sys
import time

from Crypto.PublicKey import RSA

prime1 = int(open("prime1", "r").read().strip())
prime2 = int(open("prime2", "r").read().strip())
flag = open("flag", "r").read().strip()

welcome = """
Welcome to Secure Encryption Service version 1.87
"""

# egcd copied from
# https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# flush output immediately
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
print welcome

n=prime1*prime2
e=65537L
d=modinv(e,(prime1-1)*(prime2-1))
key=RSA.construct((n,e,d,prime1,prime2))
plain=long(flag,16)

print "The public key is ("+str(e)+","+str(n)+")"
print "The encrypted flag is " + str(key.encrypt(plain,""))
