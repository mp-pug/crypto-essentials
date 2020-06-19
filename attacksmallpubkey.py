#!/usr/bin/env python3

import euclid

print("All public exponents are 3")
n1=289
n2=529
n3=319
print("Public keys contain the Moduli {},  {} and {}".format(n1,n2,n3))
c1=120
c2=413
c3=213
print("Ciphertexts are {}, {} and {}".format(c1,c2,c3))



m=n1*n2*n3

M1=m/n1
M2=m/n2
M3=m/n3


[r1,y1,t1]=euclid.eea(M1,n1)
[r2,y2,t2]=euclid.eea(M2,n2)
[r3,y3,t3]=euclid.eea(M3,n3)
# Check the values 
if r1==y1*M1+t1*n1 :
        print("y1 is {}".format(y1))
if r2==y2*M2+t2*n2 :
        y2=y2+n2
        print("y2 is {}".format(y2))
if r3==y3*M3+t3*n3 :
        print("y3 is {}".format(y3))



c=(c1*y1*M1+c2*y2*M2+c3*y3*M3)%m

# round since pow(.,(1/3)) does not give an exact value
m=round(pow(c,(1/3)))

print("c is now {}".format(c))

if c==m*m*m :
        print("m is {}".format(m))
