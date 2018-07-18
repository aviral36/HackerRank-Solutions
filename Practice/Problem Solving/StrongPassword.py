#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    special = ['!','@','#','$','%','^','&','*','(',')','-','+']
    digit = 0
    spec = 0
    lower = 0
    upper = 0
    for i in password:
        if i.isdigit():
            digit = digit+1
        elif i.islower():
            lower = lower+1
        elif i.isupper():
            upper = upper+1
        elif i in special:
            spec = spec+1
    faults = 0
    if lower == 0:
        faults = faults+1
    if upper == 0:
        faults = faults+1
    if digit == 0:
        faults = faults+1
    if spec == 0:
        faults = faults+1
    if n<6:
        gap = 6-n
        if gap>=faults:
            return gap
    return faults
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
