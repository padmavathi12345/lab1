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
def cconv(x1,x2,N):
	y=[ ]
	
	for n in range(0,N):
		sum=0
		for m in range(0,N):
			n1=n-m
			if n1<0:
			    sum=sum+(x1[m]*x2[N+(n1)])
			else:
			     sum=sum+(x1[m]*x2[(n1)])
		y.append(abs(sum))            		           
	return y

x1=input('enter sequence=')
x2=input('enter sequence=')
l=len(x1)
N=np.maximum(len(x1),len(x2))
y1=np.dot(x1,x2)
t1=dft(x1)
t2=dft(x2)
y2=cconv(t1,t2,N)
y3=np.multiply((1.0/l),y2)
print ('multiplication of two sequences=',y1)
print ('circular convolution of two DFT sequences=',y3)

plt.xlabel('-------->N')
plt.ylabel('magnitude')
plt.title('circular convolution of two DTFT sequence')
plt.stem(y3)
plt.show()			







