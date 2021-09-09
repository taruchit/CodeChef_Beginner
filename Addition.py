# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 01:01:39 2021

@author: pc
"""

T = int(input())
for tc in range(T):
	# Read integers a and b.
	(a, b) = map(int, input().split(' '))
	
	ans = a + b
	print(ans)