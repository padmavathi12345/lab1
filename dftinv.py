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
def dfti(x):
	j=cm.sqrt(-1)
	y=[ ]
	N=len(x)
	for k in range(0,N):
		w=((2*np.pi)/N)
		sum=0
		for n in range(0,N):
			sum=sum+(x[n]*np.exp(-j*w*(-k)*n))
		y.append(abs(sum))            		           
	return y

x=input('enter sequence=')
t1=dft(x)
t2=dfti(x)
print ('DFTof given sequence=',t1)
print ('DFTof inverse sequence=',t2)
plt.subplot(2,1,1)
plt.xlabel('----------->N')
plt.ylabel('Magnitude|X[k]|')
plt.title('DFTof given sequence')
plt.stem(t1)
plt.subplot(2,1,2)	
plt.xlabel('----------->N')
plt.ylabel('Magnitude|X[-k]|')
plt.title('DFTof inverse sequence')
plt.stem(t2)						
plt.show()






