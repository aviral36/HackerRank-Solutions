#!/bin/python

import sys
n = int(raw_input().strip())
for i in range(0,n-1):
    print ' '*(n-i-2), '#'*(i+1)
print '#'*n
