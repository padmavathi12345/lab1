import  numpy as np
import  matplotlib.pyplot as plt

t=np.arange(0,10,0.1)
x1=np.cos(2*np.pi*t)
plt.plot(t,x1)
plt.title("cos wave in time domain")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()
