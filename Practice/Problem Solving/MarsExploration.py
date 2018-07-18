#!/bin/python

import sys
s = raw_input().strip()
n=len(s)
signals=n/3
if s=='SOS'*signals:
    print 0
else:
    count=0
    string='SOS'*signals
    for i in range(0,n):
        if s[i]!=string[i]:
            count=count+1
    print count
