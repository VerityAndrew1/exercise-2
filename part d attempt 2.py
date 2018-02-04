# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 22:09:37 2018

@author: Verity
"""
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer

def simps1d(a,b,f,n):
                h = (b-a)/n
                n= n/2
                s = 0
                j=1
                while j<(n+1):
                    s += f(a+(h*(2*j-2)))+4*f(a+(h*(2*j-1)))+ f(a+(h*2*j))
                    j +=1 
                return((h/3)*s)
                
def expon(x, xp):
    return(np.exp(((1j*k)/(2*z))*((x-xp)**2)))

def simpswithexpon(x,a,b,n): 
    h =(b - a)/n
    n = int(n/2)
    s=0
    for i in range(1, n +1):
        s += expon(x, a+h*(2*i-2)) + 4*expon(x, a+h *(2*i-1)) + expon(x, a+h*(2*i))
    return((h/3)*s)                

def simpswithyandx(x,y,y1p,y2p,x1p,x2p,n):#eq4 fixed limits
    def simpsyp(yp):
        return(simpswithexpon(x,x1p,x2p,n)*expon(y,yp)) #first integral
    return(k*E_0/(2*np.pi*z)*simps1d(y1p,y2p,simpsyp,n)) #second integral 

def triangle(y):
    return(float(1/np.sqrt(3))*y)

def simpstriangle(x,y,n):
    def simpsyp(yp):
        return(simpswithexpon(x, triangle(-y), triangle(y),n)*expon(y,yp))
    return(k*E_0/(2*np.pi*z)*simps1d(0,4e-6,simpsyp,n))

'''def simps3d(x,y,n):#eq4 non fixed limits
    def simps2da(yp):
        return(simpseq5(x,-triangle(yp), triangle(yp),n)*func2(y,yp)) #first integral
    return(k*E_0/(2*np.pi*z)*simps1d(0,0.0001,simps2da,n)) #second integral

x1p=-0.0001
x2p=0.0001
y1p=-0.0001
y2p=0.0001'''
z=5e-3
k=1e6
E_0 = 1
n=20
start = timer()

NumPoints =100
delta =4e-6
intensity= np.zeros((NumPoints, NumPoints))
for i in range(NumPoints):
    x = i*delta
    for j in range(NumPoints):
        y = j*delta
        intensity[i,j]=abs(simpstriangle(x,y,n))**2
plt.imshow(intensity)
plt.show()
end = timer()
print("time taken to run", end-start, "s", "xmax=",xmax)



'''n=20
dx=1/NumPoints
dy = 1/NumPoints 
    
yp = np.arange(0,1,1e-3)
xplot = np.zeros((NumPoints, NumPoints))
for i in range(NumPoints):
    x= i* dx
    for j in range(NumPoints):
        y= j*dy
        xplot[i,j] = (abs(simps3d(x,y,n)))**2
plt.imshow(xplot)
plt.show()'''
'''y1p=-0.001
y2p=0.001
NumPoints = 100
y=-0.0001
x1p=-0.001
x2p=0.001

dx = 0.001 / (NumPoints -1) #does just yp need to vary? if 
dy = 0.001 / (NumPoints -1)
intensity = np.zeros( (NumPoints, NumPoints))
for i in range(NumPoints):
    x = i * dx
    for j in range(NumPoints):
        y = j* dy
        intensity[i,j] = (abs(simps3d(x,y,n)))**2
plt.imshow(intensity)
plt.show()'''








'''def expon(w,wP): #general exponential function
    return(np.exp((1j*k)/(2*z)*(w-wP**2)))

def A(yp): #examples of limit functions for a&b, circles
    return(-np.sqrt(r**2-yp**2))
def B(yp):
    return(np.sqrt(r**2-yp**2))

def X(x,A,B,n):#simpsons for X but taking A and B
    h=(B(y)-A(y))/n
    n = int(n/2)
    s=0
    for i in range(1, n +1):
        s += expon(x, A+h*(2*i-2)) + 4*expon(x, A +h *(2*i-1)) + expon(x, A+h*(2*i))
    return(abs((h/3)*s))
    

def E(y,x,c,d,n): #simpsons for y and returning total equation 4
    h = (d-c)/n
    n = int(n/2)
    s=0
    for i in range(1,n+1):
        s += expon(y,c+(h*(2*i-2))) + 4*expon(y, c +h *(2*i-1)) + expon(y, c+h*(2*i))
    return((k/(2*np.pi*z))*(abs((h/3)*s))*X(x, A,B,n))**2

NumPoints = 200
yp=np.arange(0,1,0.0001)
dx = (A(yp)-B(yp)) / (NumPoints -1)
dy = d-c / (NumPoints -1)
intensity = np.zeros( (NumPoints, NumPoints))
for i in range(NumPoints):
    x = i * dx
    for j in range(NumPoints):
        y = j* dy
        intensity[i,j] = E(y,x,c,d,n)
plt.imshow(intensity)
plt.show()'''
