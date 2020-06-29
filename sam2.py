#!/usr/bin/python3 

def multiply(x,e,n=1):
    t = 1
    while not e == 0 :
        rem = e%2
        e = e>>1
        if n > 1:
            if rem == 1:
                t = (t*x)%n
                x = (x*x)%n
        else:
             if rem == 1:
                t = t*x
                x = x*x

    return t
