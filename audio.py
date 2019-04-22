import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt

fs,d8k=wav.read('myvoice.wav')   
print(fs,len(d8k))   
print(d8k)                                    

plt.plot(d8k)
plt.show()
#wav.write('myvoice.wav',2*fs,data)