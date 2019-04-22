import numpy as np
from matplotlib import pyplot as plt
import cmath as cm

def dft(x):
	j=cm.sqrt(-1)
	y=[ ]
	N=len(x)
	for k in range(0,N):
		w=((2*np.pi)/N)
		sum=0
		for n in range(0,N):
			sum=sum+(x[n]*np.exp(-j*w*k*n))
		y.append(abs(sum))            		           
	return y
def cconv(x1,x2,l):
	y=[ ]
	
	for n in range(0,l):
		sum=0
		for m in range(0,l):
			n1=n-m
			if n1<0:
			    sum=sum+(x1[m]*x2[l+(n1)])
			else:
			     sum=sum+(x1[m]*x2[(n1)])
		y.append(abs(sum))            		           
	return y

x1=input('enter sequence=')
x2=input('enter sequence=')
l=np.maximum(len(x1),len(x2))
y1=cconv(x1,x2,l)
t1=dft(x1)
t2=dft(x2)
y2=np.abs(t1)*np.abs(t2)
print ('circular convolution of two sequence=',y1)
print ('Multiplication of DFTof two sequences=',y2)
plt.subplot(2,1,1)
plt.xlabel('----------->l')
plt.ylabel('Magnitude')
plt.title('circular convolution of given sequence')
plt.stem(y1)
plt.subplot(2,1,2)	
plt.xlabel('----------->N')
plt.ylabel('Magnitude|X1[k].X2[k]|')
plt.title('Multiplication of DFTof two sequences')
plt.stem(y2)						
plt.show()






