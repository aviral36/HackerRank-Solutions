#!/bin/python

import sys
s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))     #m is for apples
orange = map(int,raw_input().strip().split(' '))    #n is for oranges
countapple=0
countorange=0
distAppleLow=s-a
distAppleHigh=t-a
distOrangeLow=t-b
distOrangeHigh=s-b
for i in range(m):
    if apple[i]>=distAppleLow:
        if apple[i]<=distAppleHigh:
            countapple=countapple+1
for j in range(n):
    if orange[j]<=distOrangeLow:
        if orange[j]>=distOrangeHigh:
            countorange=countorange+1
print countapple
print countorange
