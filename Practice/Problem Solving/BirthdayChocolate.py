#!/bin/python

import sys

def solve(n, s, d, m):
    total=0
    for i in range(n-m+1):
        sum=0
        for j in range(m):
            sum=sum+s[i+j]
        if sum==d:
            total=total+1
    return total
           

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
