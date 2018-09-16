#!/bin/python3

import os
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    
    q = (a[d:]+a[:d])
    for i in q:
        print(i,end=" ")
