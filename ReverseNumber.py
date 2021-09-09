# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 21:46:24 2021

@author: pc
"""

#Number of testcases
T=int(input())

#Input
N=list()
for i in range(T):
    temp=int(input())
    res=0
    while temp>0:
        n=temp%10
        res=(res*10)+n
        temp=temp//10
    N.append(res)

#Output
for i in N:
    print(i)