# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 12:43:39 2021

@author: pc
"""

#Number of testcases
T=int(input())

#Input
for i in range(T):
    N=int(input())
    n=2
    Res=-1
    while(n<N):
        if(N%n==0):
            Res=1
            break
        n=n+1
    if(Res==1):
        print("no")
    else:
        print("yes")
                    