# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 17:19:50 2021

Generating next Permutation

@author: Utkarsh

Given a permutation, get the next permutation
1. Find the first decreasing value starting from the end of series
2. Swap the first decreasing value with the value which is just larger and follows the former
3. Swap the longest non-incremental suffix

"""

def next_permutation(l):
    f = False
    for i in range(len(l),0,-1):
        if l[i-1]<l[i]:
            p = i
            f = True
            break
    if not f:
        return reversed(l)
    for j in range(p+1,len(l)):
        if l[j]<l[p-1]:
            p1 = j-1
            break
    (l[p1],l[p-1]) = (l[p-1],l[p1])
    ans = l[0:p]+list(reversed(l[p]))+
    return ans


    

