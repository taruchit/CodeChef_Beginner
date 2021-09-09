# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 15:45:36 2021

@author: pc
"""

a,b= input().split()
'''
print("a: ",a) #Amount to withdraw
print("type(a): ",type(a))
print("b: ",b) #Initial balance
print("type(b): ",type(b))
'''
#Trnasforming data type
a=int(a)
#print("type(a): ",type(a))
b=round(float(b),2)
#print("type(b): ",type(b))

'''
Condition: - 
Amount to withdraw must be a multiple of 5 and lesser than initial balance.
'''

res=0

if a%5==0 and  a<b:
    res="{:.2f}".format(b-a-0.50)
else:
    res="{:.2f}".format(b)

#Balance
print(res)    


