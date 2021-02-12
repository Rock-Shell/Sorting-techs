import cv2
import numpy as np
from tkinter import *
from tkinter import messagebox
from functools import partial
import random

global font
global img
font=cv2.FONT_HERSHEY_SIMPLEX
img=np.zeros((512,1020,3),np.uint8)
n=10
global X
global N
N=np.random.randint(100,size=10)
# N=[1,2,3,4,5,6,7,8,9,10]
X=[]

def insertion(img,l):
    i=1
    msg="List is sorted upto ith i+1 th element"
    cv2.putText(img,msg,(X[0],400),font,1,(255,255,255),3,cv2.LINE_AA)
    for j in range(i,len(l)):
        img=cv2.putText(img,"Iteration: "+str(j-1),(X[0],50),font,2,(255,255,255),3,cv2.LINE_AA)
        x=j-1
        m=l[j]
        while x>=0  and m<l[x]:
            l[x+1]=l[x]
            func(img,X,i1=x+1,i2=x)
            x-=1
        l[x+1]=m
        cv2.imshow("image",img)
        cv2.waitKey(500)
        img[0:50]*=0

    print(l)
    return

def bubble(image,l):
    msg="Larger elements go backwords after each iteration"
    cv2.putText(image,msg,(X[0],400),font,1,(255,255,255),3,cv2.LINE_AA)
    for i in range(len(l)-1):
        image=cv2.putText(image,"Iteration: "+str(i),(X[0],50),font,2,(255,255,255),3,cv2.LINE_AA)
        for j in range(len(l)-1-i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                func(image,X,i1=j+1,i2=j)
        print(l)
        cv2.imshow("image",image)
        cv2.waitKey(500)
        img[0:50]*=0
    return

def selection(image,l):
    n=len(l)
    print(l)

    cv2.imshow("image",image)
    msg="smaller elements come forward after each iteration"
    cv2.putText(image,msg,(X[0],400),font,1,(255,255,255),3,cv2.LINE_AA)

    for i in range(n):
        m=i
        for j in range(i+1,n):
            if l[j]<l[m]:
                m=j
        image=cv2.putText(image,"Iteration: "+str(i),(X[0],50),font,2,(255,255,255),3,cv2.LINE_AA)
        l[i],l[m]=l[m],l[i]

        func(img,X,i1=m,i2=i)

        cv2.imshow("image",img)
        cv2.waitKey(500)
        img[0:50]*=0
        print(l)
    return

def func(image,X=X,i1=7,i2=0):
    # cv2.imshow("image",img)
    # return
    dif=X[1]-X[0]
    # print(dif)
    x=image[230:260,X[i1]:X[i1]+dif].copy()
    x2=image[230:260,X[i2]:X[i2]+dif].copy()
    y=image[300:330,X[i1]:X[i1]+dif].copy()
    image[230:260,X[i1]:X[i1]+dif]=y
    image[230:260,X[i2]:X[i2]+dif]=y
    a=0
    for i in range(i1+1-i2):
        image[170:200,X[i1]-a:X[i1]+dif-a]=x
        image[290:320,X[i2]+a:X[i2]+dif+a]=x2# shower
        cv2.imshow("image",img)
        cv2.waitKey(500)
        image[170:200,X[i1]-a:X[i1]+dif-a]=y# destroyer
        image[290:320,X[i2]+a:X[i2]+dif+a]=y
        a+=100
    image[230:260,X[i1]:X[i1]+dif]=x2
    image[230:260,X[i2]:X[i2]+dif]=x
    return

def showl(image,n=10):
    x=10
    y=256
    for i in range(n):
        X.append(x)
        x=x+ 1000//n
    for i in range(n):
        img=cv2.putText(image,str(N[i]),(X[i],y),font,1,(0,255,255),3,cv2.LINE_AA)
        cv2.imshow("image",img)
        cv2.waitKey(300)
    return img

def randomize(img=img,N=N):
    # img=zeros(img.rows,img.cols)
    random.shuffle(N)
    # img=np.zeros((512,1020,3),np.uint8)
    img*= 0
    showl(img)
    img=img
    return

img=showl(img)
window=Tk()
x="Hello fellas! Welcome to this sorting techniques project. Hope you like it, keda load koni !"
messagebox.showinfo("Sorting techniques",x)
window.wm_title("Sorting techs")
b1=Button(window,text="Selection sort",width=20,command=lambda: selection(img,N))
b2=Button(window,text="Bubble sort",width=20,command=lambda: bubble(img,N))
b3=Button(window,text="Randomize",width=20,command=lambda: randomize(img,N))
b4=Button(window,text="Insertion sort",width=20,command=lambda: insertion(img,N))
b5=Button(window,text="close",width=20,command=window.destroy)

b1.pack()
b2.pack()
b4.pack()
b3.pack()
b5.pack()

window.mainloop()
cv2.waitKey(10)
cv2.destroyAllWindows()
