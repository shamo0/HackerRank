#!/usr/bin/env python
'''
Author: shamo0

Fred is a very predictable man. For instance, when he uses his laptop, 
all he does is watch TV shows. He keeps on watching TV shows until his 
battery dies. Also, he is a very meticulous man, i.e. he pays great 
attention to minute details. He has been keeping logs of every time he
charged his laptop, which includes how long he charged his laptop for 
and after that how long was he able to watch the TV. Now, Fred wants to
use this log to predict how long will he be able to watch TV for when he 
starts so that he can plan his activities after watching his TV shows accordingly.

Challenge

You are given access to Fred’s laptop charging log by reading from the 
file “trainingdata.txt”. The training data file will consist of 100 lines,
each with 2 comma-separated numbers.

The first number denotes the amount of time the laptop was charged.
The second number denotes the amount of time the battery lasted.
The training data file can be downloaded here (this will be the same 
training data used when your program is run). The input for each of the
test cases will consist of exactly 1 number rounded to 2 decimal places. 
For each input, output 1 number: the amount of time you predict his battery will last.

Sample Input
1.50

Sample Output
3.00
'''

import math
import os
import random
import re
import sys
import numpy as np
from sklearn.linear_model import LinearRegression

timeCharged = float(input())

fd = open('trainingdata.txt','r')
fd_read = fd.readlines()
x = []
y = []
for line in fd_read:
    parts = line.split(',')
    if float(parts[0]) < 4:
        x.append(float(parts[0]))
        y.append(float(parts[1].strip()))
x = np.array(x).reshape((-1,1))
y = np.array(y)

model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)

if timeCharged >= 4:
    y_pred = 8
    print(y_pred)
else:
    y_pred = model.intercept_ + (model.coef_ * timeCharged)
    print(y_pred[0])
