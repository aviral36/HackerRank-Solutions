#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
arr1=arr[::-1]
for i in arr1:
    print i,
