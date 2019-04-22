import matplotlib.pyplot as mp
import numpy as np
m=int(input("enter the m value="))
y=[]
w=np.linspace(0,31,31)
for i in range(0,m):
	x=1
	y.append(x)
mp.stem(w,np.abs(y))
mp.title("rectangular window")
mp.xlabel("frequency")
mp.ylabel("magnitude")
mp.show()
	