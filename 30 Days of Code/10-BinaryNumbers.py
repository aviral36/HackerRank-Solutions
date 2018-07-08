#!/bin/python3

import math
import os
import random
import re
import sys

def converttobinary(n):
    binary = 0
    i = 0
    while n>0:
        remainder = n%2
        val = (10**i)*remainder
        binary = binary+val
        n = int(n/2)
        i = i+1
    return binary

if __name__ == '__main__':
    n = int(input())
    binary = converttobinary(n)
    s = str(binary)
    x = s.split('0')
    maximum = max(x)
    print(len(maximum))
        
