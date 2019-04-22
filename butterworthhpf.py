#to determine butterworth HIGH pass filter using butterworth LOW pass filter. 



import numpy as np
import matplotlib. pyplot as plt
import cmath as cm


ws=0.35*np.pi			#digital frequency
wp=0.7*np.pi
ds=0.1
dp=0.6
T=0.1

def analog(wp,ws):			#analog frequency
      Ap=((2/T)*np.tan(wp/2))
      As=((2/T)*np.tan(ws/2))
      return Ap,As

A=analog(wp,ws)
Ap=A[0]
print Ap
As=A[1]
print As


As1=Ap/As
Ap1=Ap/Ap


#order
def order(ds,dp,As1,Ap1):
       x1=((1.0/(ds**2))-1.0)
       x2=((1.0/(dp**2))-1.0)
       x=(x1/x2)
       y=(np.log(cm.sqrt(x))/np.log(As1/Ap1))
       return y

N=order(ds,dp,As1,Ap1)
n1=abs(N)
n2=np.ceil(n1)
print "order=", n2

                                                  #cutoff frequency

def    cutoff(As1,ds,n2):
         t1=(1.0/(2.0*n2))
         t2=((ds**(-2))-1.0)
         t3=t2**t1
         y=As1/t3
         return y

Ac=cutoff(As1,ds,n2)
print "cutoff frequency",Ac


          
                                        #transfer function(s')   lpf

def tf(Ac,n2,T):
      k=(n2/2)
      j=cm.sqrt(-1)
      bk=2*np.sin((((2*k)-1)*np.pi)/(2*n2))
      w=np.arange(0,np.pi,0.01)
	
      z=np.exp(j*w)
      s1=(2/T)*((1-z**(-1))/(1+z**(-1)))
      y=((Ac)**n2)/((s1**2)+(bk*Ac*s1)+(Ac**2))
      return y
hs1=tf(Ac,n2,T)
		                     #transfer function(s)    hpf
def tf(Ac,n2,T):
      k=(n2/2)
      j=cm.sqrt(-1)
      bk=2*np.sin((((2*k)-1)*np.pi)/(2*n2))
      w=np.arange(0,np.pi,0.01)
	
      z=np.exp(j*w)
      s=(2/T)*((1-z**(-1))/(1+z**(-1)))
      s1=(Ap)/s
      y=((Ac)**n2)/((s1**2)+(bk*Ac*s1)+(Ac**2))
      return y

hs=tf(Ac,n2,T)



w=np.arange(0,np.pi,0.01)

plt.plot(w,np.abs(hs))
plt.show()
       






	

