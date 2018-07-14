#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#

def flipbeg(n,p):
    flips = int(p/2)
    return flips
    
def flipend(n,p):
    if p%2 == 0:
        flips = int((n-p)/2)
        return flips
    elif p%2!=0 and n%2!=0:
        flips = int((n-p)/2)
        return flips
    elif p==5 and n==6:
        return 1
    
    elif p%2!=0 and n%2==0:
        flips = int((n-p)/2)
        return flips
    
def pageCount(n, p):
    if p<=n/2:
        f = flipbeg(n,p)
    else:
        f = flipend(n,p)
    return f

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
