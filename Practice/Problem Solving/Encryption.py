#!/bin/python3

import math
import os
import random
import re
import sys

def makeitbetter(arr):
    l = len(arr[0])
    final = []
    for i in range(l):
        a = str()
        for w in arr:
            if i<len(w):
                a=a+w[i]
            else:
                break
        final.append(a)
    return final
        

def removespaces(s):
    s.strip()
    r = s.split(' ')
    a = str()
    for i in r:
        a = a+i
    return a

# Complete the encryption function below.
def encryption(s):
    arr = removespaces(s)
    l = len(arr)
    root = math.sqrt(l)
    rows = math.floor(root)
    columns = math.ceil(root)
    result = []
    while arr!="":
        new = arr[:columns]
        arr = arr[columns:]
        result.append(new)
    final = makeitbetter(result)
    q = str()
    for f in final:
        q = q+f+' '
    return q
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
