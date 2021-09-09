# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 17:31:07 2021

@author: pc
"""
#Number of testcases
T=int(input())

#Input
N=list()

for i in range(T):
    n=int(input())
    N.append(n)
    
#Output
Res=list()

for n in N:
    temp=0
    while n>0:
        temp=temp+(n%10)
        n=n//10
    Res.append(temp)
    
#Print output
for i in Res:
    print(i)