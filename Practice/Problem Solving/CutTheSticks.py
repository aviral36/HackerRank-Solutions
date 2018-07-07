#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    l = len(arr)
    result = []
    referer = list(set(arr))
#    print('array is', arr)
    refer = sorted(referer,reverse = True)
#    print('reference is', refer)
    lr = len(refer)
    for i in range(lr):
        value = refer[i]
        result.append(arr.count(value))
#    print(result)
    for i in range(1,lr):
        result[i] = result[i]+result[i-1]
    res = result[::-1]
    for i in res:
        print(i)
        

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    cutTheSticks(arr)
