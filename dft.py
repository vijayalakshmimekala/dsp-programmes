import matplotlib.pyplot as plt
import numpy as m
p=complex(0,1)
x=[6,4,6,2,3,7]
k=[1,2,3,4,5,6]
N=1000
k=[]
for i in range(0,N-1):
	d=0
	d=d+i
X=[]
w=m.linspace(-m.pi,m.pi,N-1)
for i in range(0,N-1):
	b=0
	for n in range(0,len(x)):
		b=b+(x[n]*m.exp(-n*w[i]*2*m.pi*d*p)/N)
	X.append(b)
plt.figure(1)
plt.plot(w,m.abs(X))
plt.xlabel('frequency(w/2*m.pi)')
plt.ylabel('magnitude')
plt.title('magnitude spectrum')
plt.grid()
plt.figure(2)
plt.plot(w,m.angle(X))
plt.xlabel('freq(w/2*m.pi)')
plt.ylabel('phase angle in radian')
plt.title('phase spectrum')
plt.grid()
plt.show()