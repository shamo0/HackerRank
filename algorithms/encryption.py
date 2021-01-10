#!/bin/python3
'''
Author: shamo0

An English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text. Let 'L' be the length of this text.
Then, characters are written into a grid, whose rows and columns have the following constraints:

floor(sqrt(L)) <= row <= column < ceil(sqrt(L))

full problem description here --> https://www.hackerrank.com/challenges/encryption/problem
'''

import math
import os
import random
import re
import sys

def gridme(string, k): 
    grid = []
    for i in range(len(string)): 
        if i %k == 0: 
            sub = string[i:i+k] 
            lst = [] 
            for j in sub: 
                lst.append(j) 
            grid.append(''.join(lst))
    return(grid)

def encryption(s):
    s = s.strip()
    s = s.replace(" ","")
    length = len(s)
    
    square_root = math.sqrt(length)

    lower = math.floor(square_root)
    upper = math.ceil(square_root)
    if (lower*upper)<=length:
        lower = upper
    
    grid = gridme(s,upper)

    newstring = ""
    i=0
    j=0
    while j <= upper:
        while i < lower:
            try:
                nextLet = grid[i][j]
            except IndexError:
                i+=1
                continue
            newstring += nextLet
            
            if i == lower and j!=upper:
                upper = 0
            elif i == lower and k ==upper:
                return(newstring)
                break
            i+=1
        j+=1
        i=0
        newstring+=" "
    return(newstring)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = encryption(s)

    fptr.write(result + '\n')
    fptr.close()
