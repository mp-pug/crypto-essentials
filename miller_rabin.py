#!/usr/bin/python3

from random import randrange

def MillerRabin (p):
    d = p - 1
    r = 0
    while d % 2 == 0:
        d //=2
        r += 1
    a = randrange(2, p - 1)
    x = (a ** d) % p
    if x == 1 or x == p - 1:
        return True
    while r > 1:
        x = (x*x) % p
        if x == p-1:
            return True
        r -= 1
    return False
    