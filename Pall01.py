# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 12:29:28 2021

@author: pc
"""

#Number of testcases
T=int(input())

#Input, Computation and output
for i in range(T):
    N=input()
    N1=int(N)
    temp=N[::-1]
    N2=int(temp)
    if(N1==N2):
        print("wins")
    else:
        print("loses")
        