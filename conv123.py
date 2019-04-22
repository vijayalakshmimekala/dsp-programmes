import  matplotlib.pyplot as plt
import numpy as np
l1=int(input("enter the length of x[n]="))
l2=int(input("enter the length of h[n]="))
x=np.arange(l1)
h=np.arange(l2)
print("enter x[n] values=")
for i in range(0,l1):
	x[i]=int(input( ))
h=np.arange(l2)
print("enter h[n] values=")
for i in range(0,l2):
	h[i]=int(input( ))
y=np.arange(l1+l2-1)
for n in range(0,l1+l2-1):
	s=0
	for k in range(0,l1):
		if(n-k>=0 and n-k<l2):
			s=s+x[k]*h[n-k]
	y[n]=s
print("y[n]=",y)
