#!/bin/python

import sys
s = raw_input()
count=1
for i in s:
    if i.isupper():
        count=count+1
print count
    
