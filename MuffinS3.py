# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:59:17 2021

@author: pc
"""

#Number of testcases
T=int(input())

#Input, computation and Output
for i in range(T):
    N=int(input())
    Res=int((N/2)+1)
    #Package size that will maximize the count of left over cupckaes
    print(Res)