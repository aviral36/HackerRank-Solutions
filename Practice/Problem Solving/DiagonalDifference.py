#!/bin/python

import sys
n = int(raw_input().strip())
a = []
sumright=0
sumleft=0
for i in range(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
    sumright=sumright+(a_temp[i])
    sumleft=sumleft+(a_temp[n-i-1])
if sumright>=sumleft:
    print sumright-sumleft
else:
    print sumleft-sumright

