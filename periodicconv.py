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
print t[0]
l=7
def pconvolute(t,l):
      sum=0
      y=[ ]
      l1=4
      for i in range(0,4,1):
                  if l1>7:
                      t[l1]=0
                  sum=t[i]+t[l1]
                  l1=l1+1
                  if l1>7:
                      t[l1]=0
                  y=np.append(y,sum)  
      return y   
print t

print("convolution=", pconvolute(t,l))
