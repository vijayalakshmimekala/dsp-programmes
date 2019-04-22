import numpy as np
import matplotlib.pyplot as plt
x=input("enter samples of x=")
h=input("enter samples of h=")
lx=len(x)
lh=len(h)
m=len(x)+len(h)-1
y=np.zeros(lx)
p=[]
for i in range(0,lx):
	y[i]=x[lx-i-1]
print(y)	
for n in range(m):
	z=0
	for k in range(lx):
		if(n-k<lh and n-k>=0):
			z=z+y[i]*h[n-k]
	p=np.append(p,z)
print(p)
