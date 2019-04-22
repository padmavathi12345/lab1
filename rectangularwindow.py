import numpy as np
import  matplotlib.pyplot as plt
m=31                                           
n=np.arange(0,m)
h=[]		
for i in range(0,m,1):
	h=np.append(h,1)
plt.stem(n,h)
plt.show()