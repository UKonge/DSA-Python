# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 09:47:02 2021

Sorting algorithms

@author: Utkarsh Konge

In this code file, 4 sorting algorithms are programmed namely, selection sort, insertion sort, merge sort and quick sort.

"""

def sort_check(a):
    for i in range(1,len(a)):
        if a[i]<a[i-1]:
            print("Sorting has failed")
            return
    print("Sorting successful")
    return

def selection_sort(l): # O(n^2) performance for all cases
    for i in range(len(l)):
        m = i
        for j in range(i,len(l)):
            if l[m] > l[j]:
                m = j
        (l[m],l[i]) = (l[i],l[m])
    return

def insertion_sort(l): # Worst case performance - O(n^2). Best case - O(n)
    for i in range(len(l)):
        pos = i
        while pos > 0 and l[pos]<l[pos-1]:
            (l[pos],l[pos-1]) = (l[pos-1],l[pos])
            pos -= 1
    return


def merge(A,B):
    (C,m,n) = ([],len(A),len(B))
    (i,j) = (0,0)
    while i+j < m+n:
        if i == m:
            C.append(B[j])
            j += 1
        elif j == n:
            C.append(A[i])
            i += 1
        elif A[i] <= B[j]:
            C.append(A[i])
            i += 1
        elif A[i] > B[j]:
            C.append(B[j])
            j += 1
    return C

def merge_sort(A,l,r):
    if r-l <= 1:
        return A[l:r] 
    mid = (l+r)//2
    L = merge_sort(A, l, mid)
    R = merge_sort(A, mid, r)
    return merge(L,R)

def quick_sort(A,l,r):
    if r-l <= 1:
        return
    p = A[l]
    y = l+1
    for g in range(y,r):
        if A[g] <= A[l]:
            (A[g],A[y]) = (A[y],A[g])
            y += 1
    (A[l],A[y-1]) = (A[y-1],A[l])
    quick_sort(A,l,y-1)
    quick_sort(A,y,r)
   

a = list(range(0,500,2))+list(range(1,600,2))
ans = quick_sort(a, 0, len(a))
sort_check(a)

'''
l = list(range(500,0,-1))
l=[3,2,7]
insertion_sort(l)
print(l)
'''
