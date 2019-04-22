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
x=(1/(dp*dp))-1
print(x)#9/16
y=(1/(ds*ds))-1
print(y)#24
z=x/y#3/128
xx=c.log10(z)#1.63
print(float(abs(xx)))
dd=wp/ws#0.5
print(float(abs(dd)))
gg=c.log10(dd)#0.3
print(float(abs(gg)))
N=np.abs(0.5*(xx/gg))
print(N)
wc=np.abs(wp/((x)**(1/(2*N))))
print(wc)#17465
H=[]
for w in range(0,sample):
	hhh=1/((1+((w/wc)**(2*N))))
	H.append(hhh)
#print(np.abs(H))
plt.plot(H)
plt.show()
