# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 17:19:50 2021

Generating user defined lists

@author: Utkarsh

"""

iteratively = True

class Node:
    def __init__(self,init=None):
        self.value = init
        self.next = None
    def isempty(self):
        return (self.value==None)
    def apnd(self,v):
        if not iteratively:
            if self.isempty():
                self.value = v
            elif self.next == None:
                n = Node(v)
                self.next = n
            else:
                (self.next).apnd(v)
            return
        else:
            if self.isempty():
                self.value = v
                temp = self
                while temp.next != None:
                    temp = temp.next
                n = Node(v)
                temp.next = n
            return
    def insert(self,v):
        if self.isempty():
            self.value = v
        else:
            n = Node(v)
            (n.value,self.value) = (self.value,n.value)
            (n.next,self.next) = (self.next,n)
        return
    def delete(self,v):
        if self.empty():
            return
        if self.value == v:
            if self.next == None:
                self.value == None
            else:
                self.value = self.next.value
                self.next = self.next.next
                return
        else:
            temp = self
            while temp.next != None:
                if temp.next.value == v:
                    temp.next = temp.next.next
                    return
                else:
                    temp = temp.next
    def print_l(self):
        sl = []
        if self.isempty():
            print("List is empty")
            return
        else:
            sl = []
            temp = self
            sl.append(temp.value)
            while temp.next != None:
                temp = temp.next
                sl.append(temp.value)
            print(sl)
            return

l = Node(5)
l.apnd(10)
l.print_l()
