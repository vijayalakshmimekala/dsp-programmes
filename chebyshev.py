import numpy as np
import matplotlib.pyplot as plt
import cmath as c
import math as m
sample=30000
x=np.arange(sample)
wp=5000*np.pi
ws=8000*np.pi
dp=0.8
ds=0.2
xx=(1/(dp*dp))-1
E=xx**0.5
print(E)
x1=(1-(ds*ds))**0.5
x2=(1-((ds*ds)*(1+(E*E))))**0.5
x3=E*ds
x4=ws/wp
x5=(((x4*x4)**0.5)-1)**0.5
a1=c.log((x1+x2)/x3)
a2=c.log(x4+x5)
N1=a1/a2
print(np.abs(N1))
H2=[]
for w in range(0,sample):
	hhh=1/((1+((E**2)*(np.cos(N1*np.arccos(w/wp)))**2)))
	H2.append(hhh)
#print(np.abs(H2))
l2=len(H2)
print(l2)
H1=[]
for w in range(0,sample):
	hhh=1/((1+((E**2)*(np.cosh(N1*np.arccosh(w/wp)))**2)))
	H1.append(hhh)
#print(np.abs(H1))
l1=len(H1)
print(l1)
H=[]
for i in range(0,sample):
	hh=H2[i]+H1[i]
	H.append(hh)
print(np.abs(H))
plt.plot(H1,'b')
plt.plot(H2,'b')
plt.plot(H,'g')
plt.show()
