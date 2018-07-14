#!/bin/python

import sys
n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
colors=[]
for i in range(n):
    if ar[i] not in colors:
        colors.append(ar[i])
total=0
for i in range(len(colors)):
    flag=0
    count=0
    for j in range(n):
        if ar[j]==colors[i]:
            flag=flag+1
    count=flag/2
    total=total+count
print total
        

   
