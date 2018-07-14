#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    
    pairs = 0
    l = len(ar)
    for i in range(l):
        for j in range(i+1,l):
#            print('pair is', [ar[i],ar[j]])
            if (ar[i]+ar[j])%k == 0:
                pairs = pairs + 1
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
