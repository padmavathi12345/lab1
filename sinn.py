import  numpy as np
import  matplotlib.pyplot as plt

n=np.arange(0,10,1)
x1=np.sin(2*np.pi*n)
plt.stem(n,x1)
plt.title("sin wave in discrete domain")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()
