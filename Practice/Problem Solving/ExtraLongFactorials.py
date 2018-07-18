#!/bin/python3

import math
import os
import random
import re
import sys

def find(arr,x):
    #finds index of element x
    i = arr.index(x)
    return i 

# Complete the permutationEquation function below.
def permutationEquation(p):
    l = len(p)
    result = list()
    for x in range(1,l+1):
        y = find(p,x) + 1
        z = find(p,y) + 1
        result.append(z)
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
