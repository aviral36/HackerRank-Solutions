#!/bin/python3

import os
import sys

#
# Complete the dynamicArray function below.
#

nq = input().split()
n = int(nq[0])

q = int(nq[1])

queries = []
seqList = []
for _ in range(n):
    seqList.append([])
        
    
lastAnswer = 0

for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))

for query in queries:
    type = query[0]
    x = query[1]
    y = query[2]
    
    if type == 1:
        temp = (x^lastAnswer)%n
        seqList[temp].append(y)
    
    elif type == 2:
        temp = (x^lastAnswer)%n
        t = len(seqList[temp])
        size = y%t
        lastAnswer = seqList[temp][size]
        print(lastAnswer)
