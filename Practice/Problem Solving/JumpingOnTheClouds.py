#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count = s.count('a')
    l = len(s)
    fullstrings = int(n/l)
    result = fullstrings*count
    remainder = n%l
    partialstring = s[:remainder]
    result = result + partialstring.count('a')
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
