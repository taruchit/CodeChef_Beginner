# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 11:12:08 2021

@author: pc
"""

#Number of testcases
T=int(input())

#Input, computation and output
for i in range(T):
    N=input().split(" ")
    A=int(N[0])
    B=int(N[1])
    ResMin=0
    ResMax=int(A+B)
    if(A>B):
        ResMin=A
    elif(B>A):
        ResMin=B
    else:
        ResMin=A
    print(ResMin,"",ResMax)