# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 11:06:46 2021

@author: pc
"""

#Number of testcases
T=int(input())

#Input, computation and output
for i in range(T):
    N=input().split(" ")
    A=int(N[0])
    B=int(N[1])
    if(A>B):
        print('>')
    elif(A<B):
        print('<')
    else:
        print('=')