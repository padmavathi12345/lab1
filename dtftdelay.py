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
def dtftd(x,n0):
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
			s1=np.exp(-j*w*n0)
			sum=sum*s1
			
		y.append(abs(sum))
	return y
N=10000
p=np.linspace(0,2*np.pi,N)
x=input('enter sequence=')
n0=input('delay=')
t1=dtft(x)
t2=dtftd(x,n0)

plt.subplot(2,1,1)
plt.xlabel('-------->frequency')
plt.ylabel('magnitude|x**(jw)|')
plt.title('DTFT of given sequence')
plt.plot(p,t1)
plt.subplot(2,1,2)
plt.xlabel('-------->frequency')
plt.ylabel('magnitude|x**(jw).e**(-jwn0)|')
plt.title('DTFT of delay sequence')
plt.plot(p,t2)
plt.show()





