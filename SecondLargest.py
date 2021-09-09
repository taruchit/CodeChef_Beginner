# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 23:29:54 2021

@author: pc
"""

#Number of testcases
T=int(input())

#Input, Computation and Output
for i in range(T):
    temp=input().split(" ")
    N=list()
    N.append(int(temp[0]))
    N.append(int(temp[1]))
    N.append(int(temp[2]))
    N.sort()
    print(N[1])
        