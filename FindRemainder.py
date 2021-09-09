# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 17:53:32 2021

@author: pc
"""
#Number of testcases
T=int(input())

#Input and computation
#A=list()
#B=list()
Res=list()
for i in range(T):
    num=input().split(" ")
    a=int(num[0])
    b=int(num[1])
    #a,b=map(int, input.split(" "))
    Res.append(a%b)
    
#Output
for i in Res:
    print(i)

    