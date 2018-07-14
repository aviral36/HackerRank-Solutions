#!/bin/python3

import math
import os
import random
import re
import sys

def triggertransitionyear():
    s = '26.09.1918'
    print(s)

def Julian(year):
    if year%4==0:
        s = '12.09.'+str(year)
        print(s)
    else:
        s = '13.09.'+str(year)
        print(s)
    
def Gregorian(year):
    if year%400 == 0:
        s = '12.09.'+str(year)
        print(s)
    elif year%4 == 0 and year%100!=0:
        s = '12.09.'+str(year)
        print(s)
    else:
        s = '13.09.'+str(year)
        print(s)
    
# Complete the solve function below.
def solve(year):
    if year == 1918:
        triggertransitionyear()
    elif year < 1918:
        Julian(year)
    elif year > 1918:
        Gregorian(year)

if __name__ == '__main__':

    year = int(input())

    solve(year)

