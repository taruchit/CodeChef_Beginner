# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 18:49:21 2021

@author: pc
"""

#Number of test cases
T=int(input())

#Input and computation
#Res=list()
for i in range(T):
    num=int(input())
    count=0
    while num>0:
        temp=int(num%10)
        num=num//10
        #print("temp: ",temp)
        if(temp==4):
            count=count+1
    print(count)
    
