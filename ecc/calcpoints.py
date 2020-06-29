#!/usr/bin/python3

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




def points(a,b,p):
        y = []
        x = []
        points=[]
        for i in range(0,p):
                y.append((i*i)%p)
                x.append(((i*i*i)+a*i+b)%p)

        for i in range(0,len(x)):
                for j in range(0,len(y)):
                        if x[i] == y[j]:
                                points.append([i,j])
        return points


def ispoint(P,a,b,p):
        if (P[1]*P[1])%p != ((P[0]*P[0]*P[0])+a*P[0]+b)%p:
                return False
        else:
                return True





def ordP(P,a,b,p):
        n=1
        
        if not ispoint(P,a,b,p):
                print("Point does not lie on the curve")
                return -1
        Q=P.copy()
        
        while ispoint(Q,a,b,p) and n < 20:
                n+=1
                if Q == P:
                        s_denom = (3*(P[0]*P[0])+a)%p
                        s_nom= (2*P[1])%p
                else:
                        s_denom=(Q[1]-P[1])%p
                        s_nom=(Q[0]-P[0])%p
                
                [r,t,u]=eea(s_denom,p)
                s_denom=t%p
                while s_denom<0:
                        s_denom+=p
                s=int(s_denom*s_nom)
                Q[0]=(s*s-Q[0]-P[0])%p
                while Q[0]<0:
                        Q[0]+=p
                Q[1]=(s*int(P[0]-Q[0])-P[1])%p
                while Q[1]<0:
                        Q[1]+=p
        return n

a=9
b=10
p=11
print("All Points are given by:")
print(points(a,b,p))
P=[2,6]
print("ord(P) where P=({},{}) is  {}".format(P[0],P[1],ordP(P,a,b,p)))

Points=points(a,b,p)

for i in range(0,p):
        if ordP(Points[i],a,b,p) == 2:
                print("ord(P=({},{}))=2".format(Points[i][0],Points[i][1])) 
