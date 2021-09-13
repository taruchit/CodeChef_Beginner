# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 16:43:13 2021

@author: pc
"""

#Number of testcases
T=int(input())

#Input, computation and output
for i in range(T):
    id=input()
    if(id=='B' or id=='b'):
        print("BattleShip")
    elif(id=='C' or id=='c'):
        print("Cruiser")
    elif(id=='D' or id=='d'):
        print("Destroyer")
    else:
        print("Frigate")
        