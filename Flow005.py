# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 11:59:11 2021

@author: pc
"""

#Number of testcases
T=int(input())

#Defining the currency
one=1
two=2
five=5
ten=10
fifty=50
hundred=100

#Input, computation and Output
for i in range(T):
    count=0
    #Input
    N=int(input())
    #Computation
    while(N>0):
        if(N>=hundred):
            count=count+(N//hundred)
            N=N%hundred
        elif(N>=fifty and N<hundred):
            count=count+(N//fifty)
            N=N%fifty
        elif(N>=ten and N<fifty):
            count=count+(N//ten)
            N=N%ten
        elif(N>=five and N<ten):
            count=count+(N//five)
            N=N%five
        elif(N>=two and N<five):
            count=count+(N//two)
            N=N%two
        else:
            count=count+(N//one)
            N=N%one
    #Output        
    print(count)