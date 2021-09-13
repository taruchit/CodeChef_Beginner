# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 11:23:00 2021

@author: pc
"""

#Number of testcases
T=int(input())

#Input, computation and output
for i in range(T):
    N=input().split(" ")
    A=int(N[0])
    B=int(N[1])
    C=int(N[2])
    if((A+B+C)==180):
        print("YES")
    else:
        print("NO")