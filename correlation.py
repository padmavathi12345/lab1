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
h1=np.zeros(len(h))

t=0
for p in range (len(h)-1,-1,-1):
	h1[t]=h[p]
	t=t+1
print convolute(x,h)
print convolute(x,h1)