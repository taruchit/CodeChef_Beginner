# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 23:19:26 2021

@author: pc
"""
#Importing math module to use sqrt()
import math

#Number of testcases
T=int(input())

#Input, computation and output
for i in range(T):
    n=int(input())
    print(math.floor(math.sqrt(n)))