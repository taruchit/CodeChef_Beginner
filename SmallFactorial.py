# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 18:28:43 2021

@author: pc
"""

#Number of testcases
T=int(input())

#Input and Computation
Res=list()
for i in range(T):
    n=int(input())
    temp=1
    while(n>0):
        temp=temp*n
        n=n-1
    Res.append(temp)
    
#Output
for i in Res:
    print(int(i))
    