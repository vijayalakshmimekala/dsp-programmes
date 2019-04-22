import scipy.io.wavfile as wav
import numpy as m
from matplotlib import pyplot as plt
fs,data=wav.read('k.wav')
print(fs,len(data),data)
plt.subplot(2,1,1)
plt.plot(data)
t=m.arange(0,len(data)/fs,1.0/fs)
plt.subplot(2,1,2)
plt.plot(t,data)
plt.show( )
wav.write('k-slow',2*fs,data)