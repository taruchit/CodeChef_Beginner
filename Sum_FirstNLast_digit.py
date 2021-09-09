# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 18:14:13 2021

@author: pc
"""
#Number of testcases
T=int(input())

Res=list()

#Input and computation
for i in range(T):
    value=input()
    #print(value[0])
    #print(value[-1])
    #print(int(value[0])+int(value[-1]))
    Res.append(int(value[0])+int(value[-1]))
    
#Output
for i in Res: 
    print(i)