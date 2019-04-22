import numpy as np
from matplotlib import pyplot as plt

def convolute(x,h):
       	n1=len(x)
      	n2=len(h)
       	y=[ ]
	for n in range(n1+n2-1):
		sum=0
		for k in range(n1):
 			if n-k>=0  and  n-k<=n2-1:
				sum=sum+x[k]*h[n-k]
		y=np.append(y,sum)
	return y
x=np.array(input('entter seq1='))
h=np.array(input('entter seq2='))
t=convolute(x,h)

print("convolution=", t)
print('convolution=',np.convolve(x,h))

n1=np.arange(0,len(x),1)
n2=np.arange(0,len(h),1)
n3=np.arange(0,len(t),1)

plt.subplot(3,1,1)
plt.xlabel('------->n')
plt.ylabel('------->amplitude')
plt.title('sequence1')
plt.stem(n1,x)
plt.subplot(3,1,2)
plt.xlabel('------->n')
plt.ylabel('------->amplitude')
plt.title('sequence2')
plt.stem(n2,h)
plt.subplot(3,1,3)
plt.xlabel('------->n')
plt.ylabel('------->amplitude')
plt.title('convolution of two sequences')
plt.stem(n3,t)
plt.show()