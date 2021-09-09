# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 19:35:49 2021

@author: pc
"""

#Number of inputs
t=int(input())

#Input
N=list()

for i in range(t):
    temp=int(input())
    N.append(temp)
    
#Computation
N.sort()

#Output
for i in N:
    print(i)
    