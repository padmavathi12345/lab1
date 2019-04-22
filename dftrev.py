import numpy as np
from matplotlib import pyplot as plt
import cmath as cm

x=input('enter seq1=')


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

h=dft(x)
h1=np.zeros(len(h))

t=0
for p in range (len(h)-1,-1,-1):
	h1[t]=h[p]
	t=t+1

	
print h
print h1
plt.stem(h1)							#plt.stem(t)
plt.show()






