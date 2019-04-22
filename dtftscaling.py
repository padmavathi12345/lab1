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
def dtfts(x,m):
	j=cm.sqrt(-1)
	y=[ ]
	N=10000
	n=len(x)
	p=np.linspace(0,2*np.pi,N)
	for i in range(0,N):
		w=p[i]
		
		sum=0
		for k in range(0,n):
			sum=sum+(x[k]*np.exp(-j*w*m*k))
		y.append(abs(sum))
	return y
N=10000
p=np.linspace(0,2*np.pi,N)
x=input('enter sequence=')
m=input('m=')
t1=dtft(x)
t2=dtfts(x,m)
plt.subplot(2,1,1)
plt.xlabel('-------->frequency')
plt.ylabel('magnitude|x**(jw)|')
plt.title('DTFT of given sequence')
plt.plot(p,t1)
plt.subplot(2,1,2)
plt.xlabel('-------->frequency')
plt.ylabel('magnitude|x**(jwm)|')
plt.title('DTFT of Scaling sequence')
plt.plot(p,t2)
plt.show()




