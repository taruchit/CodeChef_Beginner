# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 11:35:04 2021

@author: pc
"""

#Input number of soilders
N=int(input())

#Input number of weapons and computation
lucky=0
unlucky=0
#weapons=list()
A=input().split(" ")
for n in A:
    if(int(n)%2==0):
        lucky=lucky+1
    else:
        unlucky=unlucky+1

#Output
if(lucky>unlucky):
    print("READY FOR BATTLE")
else:
    print("NOT READY")