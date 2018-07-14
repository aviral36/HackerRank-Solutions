#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    count = 0
    for i in a:
 #       print('i=',i)
        if i<=0:
#            print('inc count')
            count = count+1
    if count >= k:
        return 'NO'
    else:
        return 'YES'

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        r = angryProfessor(k, a)
        print(r)
