#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pickingNumbers function below.
def pickingNumbers(a):
    s = list(set(a))
    t = len(s)
    counter = []
    for i in range(t-1):
        if abs(s[i+1]-s[i]) == 1:
            x = s[i]
            y = s[i+1]
            add = a.count(x) + a.count(y)
            counter.append(add)
    
    for i in s:
        counter.append(a.count(i))
#    print('set',s)
#    print('counter',counter)
#    print('97',a.count(97))
#    print('99',a.count(99))
#    print('4', a.count(4))
#    print('5', a.count(5))
    return max(counter)
          
        
        
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
