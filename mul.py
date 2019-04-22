r1=int(input("enter the rows of matrix1"))
c1=int(input("enter the columns of matrix1"))
r2=int(input("enter the rows of matrix 2"))
c2=int(input("enter the columns of matrix 2"))
if(c1==r2):
a=[ ]
print("enter the elements of matrix1")
	for i in range (0,r1):
		for j in range(0,c1):
			a[i,j]=int(input( ))
b={ }
print("enter the elements of matrix2")
	for in range (0,r2):
		for j in range(0,c2):
			b[i,j]=int(input( ))
c={ }
	for i in range (0,r1):
		for j in range(0,c2):
			c[i,j]=0
			for k in range (0,r2):
				c[i,j]=c[i,j]+a[i,k]*b[k,j]
print("mul of matrix is")
	for i in range (0,r1):
		for j in range (0,c2):
			print[c(i,j)]
else:
print("mul is not possible")
			

