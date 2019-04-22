import numpy as np
from scipy import signal 
from matplotlib import pyplot as plt
#e[x_N]=e[x]+e[N] as e[N]=0 (since zero mean noise); we get e[x_N]=e[x] for every p samples.
p=input("order of moving average system: ")
F1=20 #INPUT FREQUENCY IN Hz
Fs=np.asarray(9000,'float32')
n=np.asarray(range(0,1000),'float32')
#x=np.sin(2*np.pi*(F1/Fs)*n)
t=np.linspace(0,1,1000,endpoint=True)
x=signal.square(2*np.pi*5*t)
#choose either noise or high freq signal(400Hz) 
#N=np.sin(2*np.pi*(400/Fs)*n)
#print(x.shape)
N=10*np.random.rand(x.shape[0])
x_N=x+N
y=[]
for i in range(0,x_N.shape[0]):
	y=np.append(y,np.sum(x_N[i:i+p])/p)

a1=plt.subplot(411)
a1.plot(x)
a2=plt.subplot(412,sharex=a1)
a2.plot(N)
a3=plt.subplot(413,sharex=a1)
a3.plot(x_N)
a4=plt.subplot(414,sharex=a1)
a4.plot(y)
plt.show()

