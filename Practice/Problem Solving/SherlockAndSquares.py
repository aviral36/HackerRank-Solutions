#!/bin/python3

import math
import os
import random
import re
import sys
    

# Complete the squares function below.
def squares(a, b):
    root_a = math.ceil(math.sqrt(a))
    root_b = math.floor(math.sqrt(b))
    results = [i for i in range(root_a,root_b+1)]
    return len(results)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
