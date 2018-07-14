#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    keyboards.sort()
    drives.sort()
    if keyboards[0] + drives[0] > b:
        return -1
    else:
        t = len(keyboards)
        l = len(drives)
        arr = []
        for i in range(t-1,-1,-1):
            for j in range(l-1,-1,-1):
                if keyboards[i]+drives[j] <= b:
                    val = keyboards[i]+drives[j]
                    arr.append(val)
                    break
        for i in range(l-1,-1,-1):
            for j in range(t-1,-1,-1):
                if keyboards[j]+drives[i] <= b:
                    valu = keyboards[j]+drives[i]
                    arr.append(valu)
                    break
        return max(arr)
        
                    
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    kb = list(map(int, input().rstrip().split()))

    dr = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(kb, dr, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
