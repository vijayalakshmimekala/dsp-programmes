
import matplotlib.pyplot as plt
import numpy as np
fs=1000
f1=f2=200
n=100
x=np.arange(n)
p=0
a=np.sin((2*np.pi*f1/fs*x)+p)
plt.subplot(311)

plt.plot(x,a)
q=45
b=np.sin((2*np.pi*f2/fs*x)+q)
plt.subplot(312)
plt.plot(x,b)
c=a+b
plt.subplot(313)
plt.plot(x,c)
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')
plt.show( )