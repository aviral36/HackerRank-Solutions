#!/bin/python

import sys
minsum=0
maxsum=0
arr = map(int, raw_input().strip().split(' '))
arr.sort()
for i in range(0,4):
    minsum=minsum+arr[i]
for j in range(1,5):
    maxsum=maxsum+arr[j]
print minsum, maxsum
    
