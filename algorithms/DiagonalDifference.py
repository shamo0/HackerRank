#!/bin/python3

'''
Author: shamo0

Given a square matrix, calculate the absolute difference between the sums of its diagonals

full problem description here: https://www.hackerrank.com/challenges/diagonal-difference/problem
'''
import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    # Write your code here
    right = 0
    left = 0
    length = len(arr)-1
    for i in range(0,len(arr)):
        left += arr[i][length]
        right += arr[i][i]
        length -= 1
    
    return(abs(left-right))    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
