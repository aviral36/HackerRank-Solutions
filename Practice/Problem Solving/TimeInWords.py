#!/bin/python3

import math
import os
import random
import re
import sys

def reference(t):
    words = {1:'one', 2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen', 15:'quarter',16:'sixteen',17:'seventeen', 18:'eighteen',19:'nineteen',20:'twenty',21:'twenty one', 22: 'twenty two', 23:'twenty three', 24:'twenty four',25:'twenty five', 26:'twenty six', 27:'twenty seven', 28:'twenty eight', 29: 'twenty nine', 30: 'half past'}
    return words[t]

# Complete the timeInWords function below.
def timeInWords(h, m):
    #hours
    time = str()
    #minutes
    if m == 0:
        hour = reference(h)
        time = hour+' '+ 'o\' clock'
    elif m>30:
        if h == 12:
            hour = 'one'
        else:
            hour = reference(h+1)
        minute = reference(60-m)
        if m != 45:
            time = minute+' minutes to '+ hour
        else:
            time = minute+' to '+ hour
    elif m==30:
        hour = reference(h)
        time = 'half past '+hour
    else:
        hour = reference(h)
        minute = reference(m)
        if m!=15 and m!=1:
            time = minute + ' minutes past '+hour
        elif m==1:
            time = minute + ' minute past '+hour
        else:
            time = minute+' past '+ hour
    return time
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
