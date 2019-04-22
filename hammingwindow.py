import numpy as np
import  matplotlib.pyplot as plt
m=31                          #32
n=np.arange(0,m)      #m-1
h=0.54-0.46*np.cos(2*np.pi*n/(m-1))
plt.stem(n,h)
plt.show()