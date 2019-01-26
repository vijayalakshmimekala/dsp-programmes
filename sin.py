import matplotlib.pyplot as plt
import numpy as np
fs=int(input("enter the value of fs"))
f1=int(input("enter the value of f1"))
f2=int(input("enter the value of f2"))
n=100
x=np.arange(n)
a=np.sin(2*np.pi*f1/fs*x)
plt.subplot(311)
plt.plot(x,a)
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')
b=np.sin(2*np.pi*f2/fs*x)
plt.subplot(312)
plt.plot(x,b)
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')
plt.show( )
plt.title('GENRATION OF SINE WAVE')
