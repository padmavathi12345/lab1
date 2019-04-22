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
x1=input("enter sequence one:")
x2=input("enter sequence two:")
y1=dtft(x1)
y2=dtft(x2)
y=np.add(np.multiply(2,y1),np.multiply(3,y2))
x=np.add(np.multiply(2,x1),np.multiply(3,x2))
y0=dtft(x)
plt.subplot(2,1,1)
plt.xlabel('--------->frequency')
plt.ylabel('Magnitude(|X1**(jw)|+|X2**(jw)|)')
plt.title('sum of DTFT of x1,x2')
plt.plot(p,(y))
plt.subplot(2,1,2)
plt.xlabel('--------->frequency')
plt.ylabel('Magnitude|X**(jw)|')
plt.title(' DTFT of x')
plt.plot(p,y0)
plt.show()





