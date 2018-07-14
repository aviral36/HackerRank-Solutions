#!/bin/python

import sys

def migratoryBirds(n, ar):
    s=list(set(ar))
    coulis=[]
    for i in s:
        coulis.append(ar.count(i))
    maxima=max(coulis)
    l=list()
    count1=coulis.count(max(coulis))
    if count1==1:
        ind=coulis.index(maxima)
        return s[ind]
    else:
        while count1!=0:
            ind=coulis.index(maxima)
            l.append(s[ind])
            l.sort()
            return l[0]
        
    
n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = migratoryBirds(n, ar)
print(result)
