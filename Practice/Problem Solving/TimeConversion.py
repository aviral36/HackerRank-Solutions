#!/bin/python

import sys
s = raw_input().strip()
reslist=[]
list=s.split(':')
if list[2][2:4]=='PM':
    if list[0]=='12':
        reslist.append(list[0])
    else:
        reslist.append(str(int(list[0])+12))       
else:
    if list[0]=='12':
        reslist.append('00')
    else:
        reslist.append(list[0])
reslist.append(list[1])
reslist.append(list[2][0:2])
a=reslist[0]+':'+reslist[1]+':'+reslist[2]
print a
    
