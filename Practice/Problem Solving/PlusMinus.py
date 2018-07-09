#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
up=0
low=0
eq=0
for i in range(n):
    if arr[i]>0:
        up=up+1
    elif arr[i]==0:
        eq=eq+1
    elif arr[i]<0:
        low=low+1
a=float(up)
b=float(low)
c=float(eq)
print a/(a+b+c)
print b/(a+b+c)
print c/(a+b+c)
        
