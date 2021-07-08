# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 11:20:27 2021

Code for GCD computation

@author: Utkarsh

2 different functions will be written to find the gcd. First will be using factors.
Second will be using Euclid's algorithm. This marks the beginning of the course.

"""

def test(A,B,fac=1):
    if fac==1:
        print("Factor method:")
        for a,b in zip(A,B):
            print("    GCD of "+str(a)+" and "+str(b)+" is "+str(gcd_factors(a, b)))
        return
    else:
        print("Euclid Method:")
        for a,b in zip(A,B):
            print("    GCD of "+str(a)+" and "+str(b)+" is "+str(gcd_euclid(a, b)))
        return


def gcd_factors(a,b):
    for i in range(min(a,b),0,-1):
        if (a%i == 0) and (b%i == 0):
            return i

def gcd_euclid(m,n):
    if m < n:
        (m,n) = (n,m)
    if m%n == 0:
        return n
    else:
        return(gcd_euclid(n, m%n))

A = [1,5,10,50,42,36,47,97]
B = [5,15,60,75,2,36,90,20]

test(A,B,2)











