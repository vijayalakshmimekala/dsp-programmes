import matplotlib.pyplot as mp
import numpy as np
m=int(input("enter the m value="))
y=[]
w=np.linspace(0,31,31)
for n in range(0,m):
	x=0.5-0.5*np.cos((2*np.pi*n)/(m-1))
	y=np.append(y,x)
mp.stem(w,np.abs(y))
mp.title("hanning window")
mp.xlabel("frequency")
mp.ylabel("magnitude")
mp.show()
	