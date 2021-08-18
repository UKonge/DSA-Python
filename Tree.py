# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 10:14:47 2021

@author: 91824
"""

class Tree:
    
    def __init__(self,init=None):
        self.value = init
        if self.value == None:
            self.right = None
            self.left = None
        else:
            self.right = Tree()
            self.left = Tree()
    
    def isempty(self):
        if self.value == None:
            return True
        return False
    
    def inorder(self):
        if self.isempty():
            return []
        else:
            return self.left.inorder()+[self.value]+self.right.inorder()
        
    def __str__(self):
        return str(self.inorder())
    
    def find(self,v):
        if self.isempty():
            return False
        if self.value == v:
            return True
        if self.value < v:
            return self.right.find(v)
        else:
            return self.left.find(v)
    
    def minval(self):
        if self.left == None:
            return self.value
        else:
            return self.left.minval()
        
    def maxval(self):
        if self.right == None:
            return self.value
        else:
            return self.right.maxval()
    
    def insert(self,v):
        if self.value == v:
            return
        if self.isempty():
            self.value = v
            self.right = Tree()
            self.left = Tree()
            return
        if self.value > v:
            self.left.insert(v)
            return
        else:
            self.right.insert(v)
            return
    
    def isleaf(self):
        return (self.left.isempty() and self.right.isempty())
    
    def makeempty(self):
        self.value = None
        self.left = None
        self.right = None
        return
    
    def cright(self):
            self.value = self.right.value
            self.right = self.right.right
            self.left = self.right.left
            return
    
    def delete(self,v):
        if self.isempty():
            return
        if v < self.value:
            self.left.delete(v)
        elif v > self.value:
            self.right.delete(v)
        else:
            if self.isleaf():
                self.makeempty()
            elif self.left.isempty():
                self.cright()
            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
        return
    

t = Tree()
for i in [1,5,2,7,11,8,54,67,42]:
    t.insert(i)
print(t)

t.insert(17)
print(t)
t.delete(7)
print(t)
