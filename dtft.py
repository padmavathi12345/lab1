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
x=input('enter sequence=')

t=0
for i in range (len(x)-1,-1,-1):
	x1[t]=h[i]
	t=t+1
print x1
	
t=dtft(x1)
plt.xlabel('-------->frequency')
plt.ylabel('magnitude|x**(jw)|')
plt.title('DTFT of given sequence')
plt.plot(p,t)
plt.show()




