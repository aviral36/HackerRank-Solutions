#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    vals = []
    for p in range(i,j+1):
        s = str(p)
        rev = s[::-1]
        t = int(rev)
        difference = abs(t-p)
        vals.append(difference)
    count = 0
    for q in vals:
        if q%k==0:
            count = count+1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
