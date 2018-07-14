#!/bin/python

import sys
def solve(q):
    if q>=38:
        r=q%5
        if r>2:
            q=q+5-r
    return q
    
    

n = input()
grades = []
modgrades=[]
for i in range(n):
    q=input()
    grades.append(q)
    modgrades.append(solve(q))
for i in range(n):
        print modgrades[i]

