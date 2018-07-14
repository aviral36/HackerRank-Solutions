#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    start = 5
    total = 0
    for i in range(n):
        likers = int(start/2)
        shares = likers*3
        start = shares
        print('day=', i)
        print('likers = ', likers)
        print('shares=', shares)
        print('start is now', start)
        total = total+likers
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
