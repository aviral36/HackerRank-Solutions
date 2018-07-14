#!/bin/python

import sys

def kangaroo(x1, v1, x2, v2):
    if x1<x2 and v1<v2:
        return 'NO'
    elif x1==x2 and v1>v2:
        return 'NO'
    elif x1==x2 and v2>v1:
        return 'YES'
    else:
        if v1!=v2:
            if (float(x1-x2)/(v2-v1))==(x1-x2)/(v2-v1):
                return 'YES'
            else:
                return 'NO'
            
        elif v1==v2:
            return 'NO'
        

x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
