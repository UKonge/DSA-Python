# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 14:33:39 2021

Backtracking module

@author: Utkarsh

The code below solved the problem of placing N queens on NxN chessboard such that no queen is under attack.
The problem is solved using backtracking.

"""

def initialize():
    n = int(input("Please enter the size of the board: "))
    board = {}
    board['n'] = n
    board['Q'] = [-1 for j in range(n)]
    board['r'] = [0 for j in range(n)]
    board['c'] = [0 for j in range(n)]
    board['inc'] = [0 for j in range(2*n-1)]
    board['dec'] = [0 for j in range(2*n-1)]
    return board

def available(i,j,board):
    n = board['n']
    return ((board['r'][i] == 0) and (board['c'][j] == 0) and (board['inc'][i+j] == 0) and (board['dec'][i-j+n-1] == 0))

def update_board(i,j,board):
    n = board['n']
    board['Q'][i] = j
    board['r'][i] = i+1
    board['c'][j] = i+1
    board['inc'][i+j] = i+1
    board['dec'][i-j+n-1] = i+1
    return

def rem_update(i,board):
    n = board['n']
    j = board['Q'][i]
    board['Q'][i] = -1
    board['r'][i] = 0
    board['c'][j] = 0
    board['inc'][i+j] = 0
    board['dec'][i-j+n-1] = 0
    return

def placeQueen(i,board):
    n = board['n']
    for c in range(n):
        if available(i,c,board):
            update_board(i,c,board)
            if i == n-1:
                return True
            else:
                e = placeQueen(i+1,board)
                if e:
                    return True
                else:
                    rem_update(i,board)
    return False

def print_ans(board):
    for i in range(board['n']):
        print(i,board['Q'][i])

def solve_nQueens():
    b = initialize()
    if b['n'] <= 3:
        print("n is less than 3, placing queens such that they do not attack each other is not possible")
        return
    placeQueen(0, b)
    print_ans(b)
    return 

solve_nQueens()