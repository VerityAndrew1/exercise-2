# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 18:31:24 2017

@author: Verity
"""
import math
import numpy as np
import matplotlib.pyplot as plt
import cmath
#defining all the functions that might be used in the menu
def simps(a,b,f,n): #basic simpsons
                h = (b-a)/n
                n= n/2
                s = 0
                j=1
                while j<(n+1):
                    s += F(a+(h*(2*j-2)),f)+4*F(a+(h*(2*j-1)),f)+ F(a+(h*2*j),f)
                    j +=1 
                return((h/3)*s)
            
def func2(x, xp):#exponential function used in integral
    return(np.exp((1j*k)/(2*z)*(x-xp)**2))

def eq5(x,a, b,n):#x integral in equation 5
             h =(b- a)/n
             n = int(n/2)
             s=0
             for i in range(1, n +1):
                 s += func2(x, a+(h*(2*i-2))) + 4*func2(x, a +h *(2*i-1)) + func2(x, a+h*(2*i))
             return(abs((h/3)*s))
         
def eq4(y,x, y1p, y2p, x1p, x2p, n):#double integral in equation 4
            h =(y2p - y1p)/n
            n = int(n/2)
            s=0
            for i in range(1, n +1):
                s += func2(y, y1p +h*(2*i-2)) + 4*func2(y, y1p +h *(2*i-1)) + func2(y, y1p +h*(2*i))
            return(eq5(x,x1p,x2p,n)*(h/3)*s)       
        
MyInput = "0"
while MyInput != "q":
    MyInput = input("Enter an option from 'a' to 'd', or 'q' to quit: ")
    
    if MyInput == "a":
        def F(x,f):#allows a function to be inputted as "f"
            return(eval(f))
        a = input("Enter a value for the lower limit, a= ")
        while not a.isdigit(): #checking a is a number
            a = input("a must be a number, please re-enter a= ")  
        b = input("Enter a value for the upper limit, b= ")
        if b == 'np.pi':
           b=(eval(b))#this is just here to let you input Pi as the upper limit for sin(x)
        else:
            while not b.isdigit(): #checking that b is a number
               b=input("b must be a number, please re-enter b= ") 
        n = input("Enter an even value for the number of terms, n= ")
        while not n.isdigit() or float(n) != int(n): #checking n is an integer
            n = input("n must be an integer, please re-enter n= ")
        f = input("Enter a function to evaluate, f= ")
        a=float(a)
        b=float(b)
        n=int(n)
        if int(n) % 2 == 0:
            print(simps(a,b,f,n))
        else:
            raise Exception("N must be a multiple of 2")
                
    elif MyInput == "b":
        while True:
            try:
                z=float(input("Enter a value for z in the order of 1e-3, z= "))
                if z< 1e-3 or z >200e-3:
                    print("Please enter a value of z between 1mm and 200mm")
                if 1e-3 <=z<= 200e-3:
                    break
            except ValueError:
                print("z must be a number")
        k=1.5e7
        x1p=0.0008
        x2p=0.001
        n = int(input("Enter an even value for n= "))
        if n % 2 == 0:
           x = np.arange(0.0007,0.0011, 1e-6) 
           y= (abs(eq5(x,x1p,x2p, 200)))**2 
           plt.plot(x,y)
           plt.show()
           print("z=",z,"n=",n)
        else:
            raise Exception ("N must be even")
    
    elif MyInput == "c" :
        z=float(input("Enter a value for z in the order of 1e-3..."))
        print("Please wait...")
        k=1e7
        x1p=-0.0001
        x2p=0.0001
        y1p=-0.0001
        y2p=0.0001
        E0 = 1
        xmin=0
        xmax=1e-3
        NumPoints = 150
        dx = xmin-xmax/ (NumPoints -1)
        dy = xmin-xmax/ (NumPoints -1)
        intensity = np.zeros((NumPoints, NumPoints))
        for i in range(NumPoints):
            x = i * dx -5*x1p #just shifting the centre of the image
            for j in range(NumPoints):
                y = j* dy -5*y1p
                intensity[i,j] = (abs((E0*k/(2*np.pi*z))*eq4(y,x,y1p,y2p,x1p,x2p,50)))**2
        plt.imshow(intensity)
        plt.show()
        
    #part d
    
    elif MyInput == "q":
        input("You have chosen to quit")
    else:
        input("That is not an option, please re-enter a choice from a to d, or q to quit: ")