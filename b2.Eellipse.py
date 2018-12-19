# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 09:23:36 2016

@author: abhinav
"""



import math as ma
a = input("Enter the value of major axis in meters : ") 
b = input("Enter the value of minor axis in meters : ") 
x1=float(input("enter the x co-ordinate of the starting point of the hole"))
y1=float(input("enter the y co-ordinate of the starting point of the hole"))
x2=float(input("enter the x co-ordinate of the ending point of the hole"))
y2=float(input("enter the y co-ordinate of the ending point of the hole"))
tt=input("enter the angle of incidence in degrees")


    

tt = tt*ma.pi/180
x = (x1+x2)/2.0 
y = (y1+y2)/2.0 
    
    
l_x = [x] 
l_y = [y] 
m = ma.tan(tt)  
def dist(x1,y1,x2,y2):
      aaa=(x2-x1)**2
      aaaa=(y2-y1)**2
      return ma.sqrt(aaa+aaaa)
c=1 
d=0
while c:
        temp1 = x
        temp2=y
        x = ( (m**2-(b/float(a))**2)*x - 2*m*y ) / ( m**2 + (b/float(a))**2 ) 
        y = ( ((b/float(a))**2-m**2)*y - 2*m*temp1*(b/float(a))**2 ) / ( m**2 + (b/float(a))**2 )
        if (y == 0):
            tt = ma.pi - tt
        else:
            tt = 2*ma.atan( -x*(b**2) / float(y*(a**2)) ) - tt
        m = ma.tan(tt)
        l_x.append(x)
        l_y.append(y)
        d=d+dist(temp1,temp2,x,y)
        
        
        if (min([y1,y2]) <= y <= max([y1,y2]) and min([x1,x2]) <= x <= max([x1,x2])):
          c=0
    
     
n= len(l_x)-2 
    
    
time_delay=d/((3.0)*10**8)

    
   
print "the no of reflections is ", n
    
print  "the time is :" , time_delay ,"seconds"
print  "the distance is :" , d ,"meters"
import pylab as pl   
pl.plot(l_x,l_y)
pl.show()

#we couldnot draw the ellipse border
