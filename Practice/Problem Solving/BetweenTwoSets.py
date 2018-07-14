#!/bin/python

import sys
n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
a = map(int, raw_input().strip().split(' '))
b = map(int, raw_input().strip().split(' '))
maxa=max(a)
minb=min(b)
lista=[]
listb=[]
for p in range(maxa, minb+1):
    counta=0
    for j in range(n):
        if p%a[j]==0:
            counta=counta+1
    if counta==n:
        lista.append(p)
for x in range(maxa, minb+1):
    countb=0
    for i in range(m):
        if b[i]%x==0:
            countb=countb+1
    if countb==m:
        listb.append(x)
total=0
for i in range(len(lista)):
    for j in range(len(listb)):
        if lista[i]==listb[j]:
            total=total+1
print total                    
