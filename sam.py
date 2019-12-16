#!/usr/bin/python3

def sam(x,p):
    p_=p
    x_=1
    k=0

    while  p_ > 0:
        if p_%2 == 1:
            x_=x_*f(x,k) 
        k=k+1
        p_=p_ >> 1

    return x_



def f(x,k):
    i = 0
    while i < k:
        x=x*x
        i=i+1
    return x 
