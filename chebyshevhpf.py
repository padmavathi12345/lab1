#chebyshev LPF (BLT)


import numpy as np
import matplotlib. pyplot as plt
import cmath as cm

			#digital requency
ws=0.35*np.pi
wp=0.7*np.pi
ds=0.1
dp=0.6
T=0.1
e=np.sqrt(((1.0/(dp**2))-1.0))
			#analog frequency
def analog(wp,ws):
      Ap=((2/T)*np.tan(wp/2))
      As=((2/T)*np.tan(ws/2))
      return Ap,As

A=analog(wp,ws)
Ap=A[0]
print Ap
As=A[1]
print As

Ap1=Ap/Ap
As1=Ap/As



                                                      #order
def order(ds,dp,As1,Ap1):
       x1=((1.0/(ds**2))-1.0)
       x2=((1.0/(dp**2))-1.0)
       x3=np.sqrt((x1/x2))
       y=(np.arccosh(x3)/np.arccosh(As1/Ap1))
       return y

N=order(ds,dp,As1,Ap1)

n2=np.ceil(N)
print "order=", n2


                                                    #transfer function

def tf(Ap1,n2,T,e):
      k=(n2/2)
      j=cm.sqrt(-1)
      k1=1/n2
      yn1=((np.sqrt(1+(e**(-2))))+(e**(-1)))**(k1)
      yn2=((np.sqrt(1+(e**(-2))))+(e**(-1)))**(-k1)
      yn=0.5*(yn1-yn2)
      cs=(np.cos((((2*k)-1)*np.pi)/(2*n2)))**(2)
      ck=(yn**(2))+cs
      bk=(2*np.sin((((2*k)-1)*np.pi)/(2*n2)))*yn
      e1=(1/(np.sqrt(1+(e**(2)))))
      w=np.arange(0,np.pi,0.01)
      z=np.exp(j*w)
      s1=(2/T)*((1-z**(-1))/(1+z**(-1)))
      y1=e1*(Ap1**(2))*ck
      y2=((s1**(2))+(bk*s1*Ap1)+((Ap1**(2))*ck))
      y=y1/y2
      return y
hs1=tf(Ap1,n2,T,e)
def tf(Ap,Ap1,n2,T,e):
      k=(n2/2)
      j=cm.sqrt(-1)
      k1=1/n2
      yn1=((np.sqrt(1+(e**(-2))))+(e**(-1)))**(k1)
      yn2=((np.sqrt(1+(e**(-2))))+(e**(-1)))**(-k1)
      yn=0.5*(yn1-yn2)
      cs=(np.cos((((2*k)-1)*np.pi)/(2*n2)))**(2)
      ck=(yn**(2))+cs
      bk=(2*np.sin((((2*k)-1)*np.pi)/(2*n2)))*yn
      e1=(1/(np.sqrt(1+(e**(2)))))
      w=np.arange(0,np.pi,0.01)
      z=np.exp(j*w)
      s=(2/T)*((1-z**(-1))/(1+z**(-1)))
      s1=Ap/s
      y1=e1*(Ap1**(2))*ck
      y2=((s1**(2))+(bk*s1*Ap1)+((Ap1**(2))*ck))
      y=y1/y2
      return y
hs=tf(Ap,Ap1,n2,T,e)
w=np.arange(0,np.pi,0.01)
plt.xlabel('------------->frequency')
plt.ylabel('Magnitude|H(e**(jw)|')
plt.title('High pass Filter')
plt.plot(w,np.abs(hs))
plt.show()
       






	

