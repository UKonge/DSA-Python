# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 10:48:07 2021

@author: Utkarsh

The Problems to be solved here are
1. Binary Knapsack optimziation
2. Subset sum problem
3. Equal sum partition
4. Count the number of subset with given sum
5. Minimum subset difference
6. Count the number of subset given the difference
7. Target sum
"""


#%%
'''
2. Subset sum problem:
    Given an array of integers, state if there exist a subset of array with the given sum
'''

def subsetProb(arr,s):
    n = len(arr)
    t = [[False for _ in range(s+1)] for _ in range(n+1)]
    for i in range(n+1):
        t[i][0] = True
    for i in range(1,n+1):
        for j in range(1,s+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][s]

# test cases
arrs = [[4,5,6,1,10,19,6],[1,2,3,4,5,10],[5],[6,7]]
ss= [[9,20,67,2],[6,7,50],[5,6],[3,13]]
for i in range(len(arrs)):
    print("Test case",i+1)
    ans = []
    for j in range(len(ss[i])):
        print("    Sub-test case",j+1)
        print("    ",subsetProb(arrs[i], ss[i][j]))
    print(" ")

#%%