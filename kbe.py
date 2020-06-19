#!/usr/bin/env python3

import math

def computekbe(x,n):
	q=[]
	r=[]
	q.append(math.floor(x))
	r.append(x-q[0])
	i=0
	while r[i] != 0 and i < n :
		q.append(math.floor(1/r[i]))
		r.append((1/r[i])-q[i+1])
		i+=1
	return q 

def returnapproxfrac(q,n=-1):
	if n == -1 :
		n=len(q)
	
	if n == 0:
		return [q[0],1]
	
	if n == 1:
		return [ q[0]*q[1]+1,q[1]] 

	n1=q[0]
	n2=q[0]*q[1]+1

	d1=1
	d2=q[1]
	for i in range(2,n+1):
		n_iter=q[i]*n2+n1
		d=q[i]*d2+d1

		n1=n2
		n2=n_iter

		d1=d2
		d2=d

	return [n_iter,d] 

xval=math.sqrt(40913)

size=25


x = computekbe(xval,size)
print("KBE of  {} is {} .".format(xval,x))
n=[] 
d=[]
for i in range(0,size):
	[nt,dt]=returnapproxfrac(x,i)
	n.append(nt)
	d.append(dt)
	print("{}-th Approximation : {}/{}".format(i,nt,dt))

for i in range(0,size):
	print("{}^2 = {}  mod 40913".format((n[i]%40913), (n[i]*n[i])%40913))

