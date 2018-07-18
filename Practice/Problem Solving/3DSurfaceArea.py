#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A, H, W):
    TSA = 0
    for i in range(H):
        for j in range(W):
            #adding top and bottom
            TSA = TSA+2
            #computing east
            if j==W-1:
                TSA = TSA+A[i][j]
            else:
                if A[i][j]>A[i][j+1]:
                    TSA = TSA + (A[i][j]-A[i][j+1])
            #computing west
            if j==0:
                TSA = TSA+A[i][j]
            else:
                if A[i][j]>A[i][j-1]:
                    TSA = TSA + (A[i][j]-A[i][j-1])
            #computing north
            if i==0:
                TSA = TSA+A[i][j]
            else:
                if A[i][j]>A[i-1][j]:
                    TSA = TSA + (A[i][j]-A[i-1][j])
            #computing south
            if i==H-1:
                TSA = TSA+A[i][j]
            else:
                if A[i][j]>A[i+1][j]:
                    TSA = TSA + (A[i][j]-A[i+1][j])
    return TSA
                
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A, H, W)

    fptr.write(str(result) + '\n')

    fptr.close()
