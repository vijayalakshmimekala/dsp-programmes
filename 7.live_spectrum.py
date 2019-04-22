import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
import sounddevice as sd
fs,data=wav.read('myvoice8.wav');data=data[:,0]
#fs=600;x=2*np.pi*np.arange(1000)/fs;data=np.concatenate((np.sin(10.0*x),np.sin(50.0*x),np.sin(10.0*x)+np.sin(50.0*x)),axis=0)
plt.plot(data);plt.show()
t=range(0,len(data))
winl=0.01*fs
nwin=int(len(data)/winl)
winl=int(winl)
N=int(2**np.ceil(np.log2(winl)))
F=np.arange(0,N/2)*fs/N
plt.ion()
for i in range(nwin):
    r=np.array(range(i*winl,(i+1)*winl))
    x=data[r]
    #sd.play(data[r+winl], fs)
    X=np.fft.fft(x,N)
    X_mag=np.abs(X)
    plt.subplot(211)
    plt.plot(t,data,r,x)         
    plt.subplot(212)
    plt.plot(F,X_mag[0:N/2])
    plt.xlabel('frequency in Hz')         
    plt.draw()
    plt.pause(0.1)     
    plt.clf()
