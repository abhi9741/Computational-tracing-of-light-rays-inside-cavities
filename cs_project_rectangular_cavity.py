# -*- coding: utf-8 -*-
"""
Created on Wed Nov 09 23:31:50 2016

@author: Abhinav
"""

l=float(input("enter the lenght of the rectangle in meters"))
b=float(input("enter the width of the rectangle in meters"))
#taking points in clock wise starting from (0,0)
x1=0
y1=0
x2=0
y2=b
x3=l
y3=b
x4=l
y4=0
xh=float(input("enter the x coordinate of the hole"))
yh=float(input("enter the y coordinate of the hole"))
h=float(input("enter the lenght of the hole"))
import math
p=math.pi 
kj=int(input("type 1 for entering angle in degrees or type  2 for entering angle in radians"))

if kj==1:
    theta1=input("enter the angle in degrees")
    temp=theta1
    import math
    pi=math.pi
    theta1=(temp*pi)/180
if kj==2:    
      theta1=input("enter the angle in radians")
if theta1 >p:
    theta1=theta1%p
if theta1 <0:
      import math
      p=math.pi
      theta1=p+theta1
      

hh=h/2

# iam just importing the function line satisfyit has nothing to do with the flow


def linesatisfy(x,y):
    
             if (y-y1)*(x2-x1)-(y2-y1)*(x-x1)==0:
            
                 return 1
  
             if (y-y2)*(x3-x2)-(y3-y2)*(x-x2)==0:
           
                 return 2
    
             if (y-y3)*(x4-x3)-(y4-y3)*(x-x3)==0:
             
                 return 3
   
             if (y-y4)*(x1-x3)-(y4-y1)*(x-x4)==0:
            
                 return 4




#generating limit points
if linesatisfy(xh,yh)==1:
    xh1=xh
    xh2=xh
    yh1=yh+h/2
    yh2=yh-h/2
if linesatisfy(xh,yh)==2:
    xh1=xh+h/2
    xh2=xh-h/2
    yh1=yh
    yh2=yh
if linesatisfy(xh,yh)==3:
    xh1=xh
    xh2=xh
    yh1=yh+h/2
    yh2=yh-h/2
if linesatisfy(xh,yh)==4:
    xh1=xh+h/2
    xh2=xh-h/2
    yh1=yh
    yh2=yh
# iam just importing the fow function(on which line the given ray intersects based on this we are gonna find reflection point)




#fow=finding on which side point intersects
t=theta1
def fow(x,y,t):
    import math 
    p=math.pi 
    p=float(p)
    l=linesatisfy(x,y)
    if t <0:
        t=p+t
    if l==1:
        m1=float(y3-y)/float(x3-x)
        m2=float(y4-y)/float(x4-x)
        t1=math.atan(m1)
        t2=math.atan(m2)
        if t1<0:
            t1=t1+p
        if t2<0:
            t2=t2+p
        if t<0:
            t=p+t
        if (t<t1) and (t>0):
            return 3
        
        if (t<p/2.0) and (t>t1):
            return 2
        
        if (t<t2) and (t>p/2.0):
            return 4
        
        if (2.0*p) and (t>t2):
            return 3
        
    if l==2:
        m1=float(y1-y)/float(x1-x)
        m2=float(y-y4)/(x-x4)
        t1=math.atan(m1)
        t2=math.atan(m2)
        if t1<0:
            t1=t1+p
        if t2<0:
            t2=t2+p
        if (t<t1) and (t>0):
            return 1
        
        if (t<t2) and (t>t1):    
            return 4
        
        if (t<p) and (t>2):
            return 3
        
        
        if (t<p+1.0) and (t>p):
            return 1
        
        if (t<p+t2) and (t>p+t1):
            return 4
      
        if (t<2*p) and (t>p+t2):
            return 3
     
    if l==3:
        m1=float(y-y1)/float(x-x1)
        m2=float(y-y2)/float(x-x2)
        t1=math.atan(m1)
        t2=math.atan(m2)
        if t1<0:
            t1=t1+p
        if t2<0:
            t2=t2+p
        if (t<t1) and (t>0):
            return 1
        
        if (t<p/2) and (t>t1):
            return 4
  
        if (t<t2) and (t>p/2):
            return 2
        
        if (t<2*p) and (t>t2):
            return 1
  
    if l==4:
        m1=float(y-y3)/float(x-x3)
        m2=float(y-y2)/float(x-x2)
        t1=math.atan(m1)
        t2=math.atan(m2)
        if t1<0:
            t1=t1+p
        if t2<0:
            t2=t2+p
        if (t<t1) and (t>0):
            return 3
        
        if (t<t2) and (t>t1):
            return 2
        
        if (t<p) and (t>t2):
            return 1
        
        
        if (t<p+t1) and (t>p):
            return 3
      
        if (t<p+t2) and (t>p+t1):
            return 2
       
        if (t<2*p) and (t>p+t2):
            return 1
         
           
            
#now iam gonnna import the ref pt function it has nothing to do with the work flow            


def refptx(x5,y5,t):
       
       import math 
       m=math.tan(t)
       
       f=fow(x5,y5,t)
       
       if f==1:
            a1=1
            b1=0
            c1=0
            a2=float(m)
            b2=-1
            c2=float(y5)-float(m*x5)
            aa1=(b1*c2)-(b2*c1)
            bb=(a1*b2)-(a2*b1)
            aa2=(c1*a2)-(c2*a1)
            aa1=float(aa1)
            bb=float(bb)
            x6=aa1/bb
            return x6
    
       if f==2:
            a1=0
            b1=1
            c1=-b 
            a2=float(m)
            b2=-1
            c2=float(y5)-float(m*x5) 
            aa1=(b1*c2)-(b2*c1)
            bb=(a1*b2)-(a2*b1)
            aa2=(c1*a2)-(c2*a1)
            aa1=float(aa1)
            bb=float(bb)
            x6=aa1/bb
            return x6
     
       if f==3:
            a1=1
            b1=0
            c1=-l
            a2=float(m)
            b2=-1
            c2=float(y5)-float(m*x5) 
            aa1=(b1*c2)-(b2*c1)
            bb=(a1*b2)-(a2*b1)
            aa2=(c1*a2)-(c2*a1)
            aa1=float(aa1)
            bb=float(bb)
            x6=aa1/bb
            return x6
            
       if f==4:
            a1=0
            b1=1
            c1=0 
            a2=float(m)
            b2=-1
            c2=float(y5)-float(m*x5) 
            aa1=(b1*c2)-(b2*c1)
            bb=(a1*b2)-(a2*b1)
            aa2=(c1*a2)-(c2*a1)
            aa1=float(aa1)
            bb=float(bb)
            x6=aa1/bb
            return x6

    
def refpty(x5,y5,t):
       
       import math
       
       m=math.tan(t)
       
       f=fow(x5,y5,t)
       
       if f==1:
            a1=1
            b1=0
            c1=0
            a2=float(m)
            b2=-1
            c2=float(y5)-float(m*x5)
            aa1=(b1*c2)-(b2*c1)
            bb=(a1*b2)-(a2*b1)
            aa2=(c1*a2)-(c2*a1)
            aa2=float(aa2)
            bb=float(bb)
            y6=aa2/bb
            return y6
      
    
       if f==2:
          a1=0
          b1=1
          c1=-b 
          a2=float(m)
          b2=-1
          c2=float(y5)-float(m*x5) 
          aa1=(b1*c2)-(b2*c1)
          bb=(a1*b2)-(a2*b1)
          aa2=(c1*a2)-(c2*a1)
          aa2=float(aa2)
          bb=float(bb)
          y6=aa2/bb
          return y6

       if f==3:
          a1=1
          b1=0
          c1=-l 
          a2=float(m)
          b2=-1
          c2=float(y5)-float(m*x5)  
          aa1=(b1*c2)-(b2*c1)
          bb=(a1*b2)-(a2*b1)
          aa2=(c1*a2)-(c2*a1)
          aa2=float(aa2)
          bb=float(bb)
          y6=aa2/bb
          return y6

       if f==4:
          a1=0
          b1=1
          c1=0 
          a2=float(m)
          b2=-1
          c2=float(y5)-float(m*x5)
          aa1=(b1*c2)-(b2*c1)
          bb=(a1*b2)-(a2*b1)
          aa2=(c1*a2)-(c2*a1)
          aa2=float(aa2)
          bb=float(bb)
          y6=aa2/bb
          return y6
    
h=refptx(xh,yh,t)
k=refpty(xh,yh,t)

def check(x,y):
    if (x<=xh1) and (x>=xh2) and (y<=yh1) and (y>=yh2):
        return False 
    else :
        return True 
def dist(x1,y1,x2,y2):
      aaa=(x2-x1)**2
      aaaa=(y2-y1)**2
      return math.sqrt(aaa+aaaa)
c=0
d=0
x_cord=[xh,h]
y_cord=[yh,k]
import math
p=math.pi 
while check(h,k):
       temp1=h
       temp2=k
       t=p-t
       h=refptx(temp1,temp2,t)
       k=refpty(temp1,temp2,t)
       c=c+1
       d=d+dist(temp1,temp2,h,k)
       x_cord.append(h)
       y_cord.append(k)
       if (h==0) and (k==0):
           d=2*d
           break
       if (h==0) and (k==b):
           d=2*d
           break
       if (h==l) and (k==b):
           d=2*d
           break
       if (h==l) and (k==0):
           d=2*d
           break
       
      
print "total number of reflections is" , c 
print "total distance travelled by the light ray inside te rectangle is", d , "meters"
ttt=3.0*(10**8)
time_delay=d/ttt
print "the time delay is " , time_delay , "seconds"
import pylab as pl
print "if you can close the hole before ", time_delay ,"seconds then you can store the light ray for infinite time(it is assumed that there is no energy loss at every reflection)"

print "the path of light inside the cavity"
x_cord=tuple(x_cord)
y_cord=tuple(y_cord)
pl.plot(x_cord,y_cord)
pl.show()












