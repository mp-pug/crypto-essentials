#!/usr/bin/env python3

import random
import euclid 
import sam2 
import miller_rabin
import sys
sys.stdout=open("/home/app/results/results.log","w")



## Factorizes n=p*q for known, n,e,d
def factorize(n,e,d):
	s=0
	s2=2
	u=e*d-1
	while u%2 == 0:
		s=s+1
		s2*=2
		u/=2
	g=1
	u=int(u)	
	if pow(2,s)*u == e*d-1 and u%2 == 1:
		print("Decomposition ok")
		print("s is {}".format(s))
		print("u is {}".format(u))
		print("e*d-1 is {}".format(e*d-1))
	while g ==1 or g==n:
		a=random.randrange(1,n)
		print("New Value for a generated : {}".format(a))
		ggT=euclid.gcd(a,n)
		print("gcd(a,n)={}".format(ggT))
		if ggT != 1:
			return [a, n/a ]
		au=sam2.multiply(a,u,n)
		print("a^u is : {}".format(au))
		for j in range(0,s):
			g=euclid.gcd(sam2.multiply(au,pow(2,j),n)-1,n) 
			print("Iteration {}: {}".format(j,g))
			if g != 1 and g != n:
				return [g, n/g]


# Tests by simple division if the current value divides n
def simpledivision(n):
	for t in range(2,n):
		if round(n/t) == n/t :
			return [t,n/t] 


# Uses the p-1 Method by J.M. Pollard











# Initial Values for testing

n=2731043227879

e=17

d=1927792861073

values=factorize(n,e,d)
print("Computed factors are {} and {}".format(values[0],values[1]))
if values[0]*values[1] == n :
	print("Test OK")
else:
	print("Test NOK")




