import  numpy as np
import  matplotlib.pyplot as plt

t=np.arange(0,10,0.1)
x=np.log(t)
plt.stem(t,x)
plt.title("ramp function")
plt.xlabel("time")
plt.ylabel("amplitude")


plt.show()
