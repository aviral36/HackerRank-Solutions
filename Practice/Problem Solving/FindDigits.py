#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    result = 0
    number = n
    while n>0:
        print('n is', n)
        digit = n%10
        if digit != 0:
            if number%digit == 0:
                result = result + 1
        print('digit is', digit)
        print('result is', result)
        n = int(n/10)
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
