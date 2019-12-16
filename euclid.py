#!/usr/bin/python3



def gcd (a,b):
    if a > b :
        r1=a
        r2=b
    else:
        r1=b
        r2=a
    while not r2 == 0:
        r = r1%r2
        r1=r2
        r2=r

    return r1


def eea(a,b):
    if a > b :
        r1=a
        r2=b
    else:
        r1=b
        r2=a

    s1=1
    s2=0
    t1=0
    t2=1
    while not r2 == 0:
        r = r1%r2
        q = (r1-r)/r2
        s = s1 -q*s2
        t = t1-q*t2
        
        s1=s2
        s2=s

        t1=t2
        t2=t 

        r1=r2
        r2=r

    if a > b: 
        return [r1, s1 ,t1 ] 
    else:
        return [r1,t1,s1]





