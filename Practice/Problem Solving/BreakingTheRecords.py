#!/bin/python

import sys

def recordLow(s):
    l=len(s)
    low=s[0]
    record=0
    for i in range(1,l):
        if s[i]<low:
            record=record+1
            low=s[i]
    return record
def recordHigh(s):
    l=len(s)
    high=s[0]
    record=0
    for i in range(1,l):
        if s[i]>high:
            record=record+1
            high=s[i]
    return record
        

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
low=recordLow(s)
high=recordHigh(s)
print high, low
