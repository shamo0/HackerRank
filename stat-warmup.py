'''
You are given an array of N integers separated by spaces, all in one line.

Display the following:

Mean (m): The average of all the integers.

Median of this array: In case, the number of integers is odd, 
the middle element; else, the average of the middle two elements.

Mode: The element(s) which occurs most frequently. If multiple 
elements satisfy this criteria, display the numerically smallest one.

Standard Deviation (SD).
SD = (((x1-m)2+(x2-m)2+(x3-m)2+(x4-m)2+...(xN-m)2))/N)0.5

where xi is the ith element of the array

Lower and Upper Boundary of the 95% Confidence Interval for the mean, 
separated by a space. This might be a new term to some. However, it is
an important concept with a simple, formulaic solution. Look it up!
'''
import math
import statistics 
import numpy as np
import scipy.stats
from scipy import stats as s

def mean_confidence_interval(mean,sd,data):
    lower_confidence = mean-1.96*sd/len(data)**0.5
    upper_confidence = mean+1.96*sd/len(data)**0.5
    tup = (lower_confidence,upper_confidence)
    return(tup) 
    
def standard_Deviation(mean,test_list):
    variance = sum([((x - mean) ** 2) for x in test_list]) / len(test_list) 
    res = variance ** 0.5
    return(res)

lineOne = int(input())
lineTwo = input()

items = lineTwo.split(' ')
numbers = []

for i in items:
    numbers.append(int(i.strip()))

mean = statistics.mean(numbers)
median = statistics.median(numbers)
mode = int(s.mode(numbers)[0]) # takes care of no unique number case
standardDev = standard_Deviation(mean,numbers)
confidenceInterval = mean_confidence_interval(mean,standardDev,numbers)

print("{:.1f}".format(mean))
print("{:.1f}".format(median))
print(mode)
print("{:.1f}".format(standardDev))
print("{:.1f}".format(confidenceInterval[0]),"{:.1f}".format(confidenceInterval[1]))
