#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arr1 = arr[::-1]
    for i in arr1:
        print(i,end=' ')
