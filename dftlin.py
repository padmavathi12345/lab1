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

x1=input('enter sequence=')
x2=input('enter sequence=')
y1=dft(x1)
y2=dft(x2)
y=np.add(np.multiply(2,y1),np.multiply(3,y2))
x=np.add(np.multiply(2,x1),np.multiply(3,x2))
y0=dft(x)
print ('sum of  individual two DFT  sequences =',y)
print ('DFT of sum of sequence=',y0)
plt.subplot(2,1,1)
plt.xlabel('--------->frequency')
plt.ylabel('Magnitude(|X1(k)|+|X2(k)|)')
plt.title('sum of DFT of x1,x2')
plt.stem(y)
plt.subplot(2,1,2)
plt.xlabel('--------->frequency')
plt.ylabel('Magnitude|X(k)|')
plt.title(' DFT of x')
plt.stem(y0)
plt.show()		







