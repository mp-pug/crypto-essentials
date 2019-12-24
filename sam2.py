#!/usr/bin/python3 

def multiply(x,e):
    t = 1
    while not e == 0 :
        rem = e%2
        e = e>>1
        if rem == 1:
            t = t*x
        x = x*x
    return t
