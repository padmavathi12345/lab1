import numpy as np
from matplotlib import pyplot as plt
import cmath as cm

def dtft(x):
	j=cm.sqrt(-1)
	y=[ ]
	N=10000
	n=len(x)
	p=np.linspace(0,2*np.pi,N)
	for i in range(0,N):
		w=p[i]
		
		sum=0
		for k in range(0,n):
			sum=sum+(x[k]*np.exp(-j*w*k))
		y.append(abs(sum))
	return y
N=10000
p=np.linspace(0,2*np.pi,N)
x1=input('enter sequence=')
x2=input('enter sequence=')
n=len(x1)+len(x2)-1
n1=np.arange(0,n)
t1=dtft(x1)
t2=dtft(x2)
t=np.abs(t1)*np.abs(t2)
y=np.convolve(x1,x2)
plt.subplot(2,1,1)
plt.xlabel('-------->frequency')
plt.ylabel('magnitude of y')
plt.title('convolution of given sequence')
plt.plot(n1,y)
plt.subplot(2,1,2)
plt.xlabel('-------->frequency')
plt.ylabel('magnitude|x**(jw)|')
plt.title('multiplication of DTFT of two sequence')
plt.plot(p,t)
plt.show()




