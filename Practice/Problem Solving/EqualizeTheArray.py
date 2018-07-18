#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    counts = []
    s = list(set(arr))
    print('s is', s)
    for i in s:
        counts.append(arr.count(i))
    print('counts is', counts)
    maxcount = max(counts)
    ind = counts.index(maxcount)
    value = s[ind]
    print('maxcount is', maxcount)
    print('index is', ind)
    print('value is', value)
    l = len(arr)
    p = arr.count(value)
    print('l is', l)
    print('p is', p)
    return l-p
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
