# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 00:43:14 2021

@author: pc
"""

T=input()
T=int(T)

#print(type(T))

A=list()
B=list()
Res=list()

for i in range(T):
    data=input()
    data=data.split(" ")
    #a=int(data[0])
    #b=int(data[1])
    #A.append(a)
    #B.append(b)
    A.append(int(data[0]))
    B.append(int(data[1]))
    #Res[i]=A[i]+B[i]
    
for i in range(T):
    print(A[i]+B[i])
    