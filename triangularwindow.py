import numpy as np
import matplotlib.pyplot as plt
m=31
n=np.arange(0,m)
a=(m-1)/2.0
b=np.abs(n-a)
c=2.0*b
d=c/(m-1)
e=1.0-d
plt.stem(n,e)
plt.show()
