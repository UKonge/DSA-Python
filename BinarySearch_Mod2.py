# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 11:20:27 2021

Binary Search

@author: Utkarsh

Basic code for binary search

"""

def bin_search(seq,v,l,r):
    if r == l:
        return False
    mid = (r+l) // 2
    if v == seq[mid]:
        return True
    if v > seq[mid]:
        return bin_search(seq, v, mid+1, r)
    else:
        return bin_search(seq, v, l, mid)

v = 0
s = [1,2,3,4,5,6,7,8,19,30]
print(bin_search(s, v, 0, len(s)))