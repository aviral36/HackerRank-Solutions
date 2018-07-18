#!/bin/python3

import math
import os
import random
import re
import sys

def shift(a,l,k):
    s = int(k%l)
    sp = l-s
    new = a[sp:]+a[:sp]
#    print(new)
    return new


# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    l = len(a)
    arr=list()
    if k==l:
        arr = a
    else:
        arr = shift(a,l,k)
    result = []
    for query in queries:
        result.append(arr[query])
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
