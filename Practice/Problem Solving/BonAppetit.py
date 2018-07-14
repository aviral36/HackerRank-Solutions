#!/bin/python

import sys

def bonAppetit(n, k, b, ar):
    sum=0
    for i in range(n):
        if i!=k:
            sum=sum+ar[i]
        else:
            sum=sum+0
    bac=(sum)/2
    if bac==b:
        return 'Bon Appetit'
    else:
        return b-bac

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
b = int(raw_input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
