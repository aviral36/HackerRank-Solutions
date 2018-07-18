#!/bin/python3

import math
import os
import random
import re
import sys

def alternating(array):
    l = len(array)
    f = 0
    for i in range(l-1):
        if array[i] == array[i+1]:
            f = 1
    return f

def makearray(s, x, y):
    temp = []
    for i in s:
        if i==x or i==y:
            temp.append(i)
    return temp
    
# Complete the twoCharaters function below.
def twoCharaters(s):
    l = list(set(s))
    sets = []
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            sets.append([l[i],l[j]])
    resultarray = []
    for i in range(len(sets)):
        x = sets[i][0]
        y = sets[i][1]
        array = makearray(s, x, y)
        flag  = alternating(array)
        if flag == 0:
            resultarray.append(len(array))
    if resultarray == []:
        return 0
    else:
        return max(resultarray)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input())

    s = input()

    result = twoCharaters(s)

    fptr.write(str(result) + '\n')

    fptr.close()
