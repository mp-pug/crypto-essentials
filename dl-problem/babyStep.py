#!/usr/bin/python3 


from math import *
import euclid as euclid


def babyStepGiantStep(a,g,n,ordg):
	ng=floor(sqrt(ordg))
	a_inv=euclid.inv(a,n)
	g_1=[]
	for i in range(0,ng+1):
		g_1.append(pow(g,i)%n)


	for i in range(0,ng+1):
		g_2=(a*euclid.inv(pow(g,i*ng),n))%n
		for j in range(0,ng+1):
			if g_2==g_1[j]:
				return [j,i] 




a = 67
g=5
n=103
ordg=103
[x0,x1 ] = babyStepGiantStep(a,g,n,ordg) 

x = x0+ floor(sqrt(ordg))*x1
if 67 == (pow(g,x))%n :
	print("Test OK")
	print("x is {}".format(x))





