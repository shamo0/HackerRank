'''
Given five positive integers, find the minimum and maximum values that 
can be calculated by summing exactly four of the five integers. Then 
print the respective minimum and maximum values as a single line of two
space-separated long integers.
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):

    arr = sorted(arr)
    lowerSum = 0
    higherSum = 0
    for i in range(0,4):
        lowerSum += int(arr[i])
        higherSum += int(arr[-i-1])
    print(lowerSum,higherSum)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
