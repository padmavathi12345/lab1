import  numpy as np
import  matplotlib.pyplot as plt

t=np.arange(-10,10,0.1)
x=np.sinc(t)
plt.stem(t,x)
plt.title("sinc function")
plt.xlabel("time")
plt.ylabel("amplitude")


plt.show()
