#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximizingXor function below.
def maximizingXor(l, r):
    result = []
    for num1 in range(l,r+1):
        for num2 in range(l,r+1):
            xor = num1^num2
            result.append(xor)
    return max(result)
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
