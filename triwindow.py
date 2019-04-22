import matplotlib.pyplot as mp
import numpy as np
m=int(input("enter the m value="))
y=[]
w=np.linspace(0,31,31)
for n in range(0,m):
	x=1-(2*np.abs(n-(m-1)/2))/(m-1)
	y=np.append(y,x)
mp.stem(w,np.abs(y))
mp.title("triangular window")
mp.xlabel("frequency")
mp.ylabel("magnitude")
mp.show()
	