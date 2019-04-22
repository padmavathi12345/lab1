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
def dtftdif(x,m):
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
			s1=1-(np.exp(-j*w*m))
			sum=sum*s1
			
		y.append(abs(sum))
	return y
N=10000
p=np.linspace(0,2*np.pi,N)
x=input('enter sequence=')
m=input('delay=')
t1=dtft(x)
t2=dtftdif(x,m)

plt.subplot(2,1,1)
plt.xlabel('-------->frequency')
plt.ylabel('magnitude|x**(jw)|')
plt.title('DTFT of given sequence')
plt.plot(p,t1)
plt.subplot(2,1,2)
plt.xlabel('-------->frequency')
plt.ylabel('magnitude|x**(jw).[1-e**(-jwm)]|')
plt.title('DTFT of difference sequence')
plt.plot(p,np.abs(t2))
plt.show()





