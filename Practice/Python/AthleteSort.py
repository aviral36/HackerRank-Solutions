#!/bin/python

import sys

if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    arr = []
    for arr_i in xrange(n):
        arr_temp = map(int,raw_input().strip().split(' '))
        arr.append(arr_temp)
    k = int(raw_input().strip())
    templist=[]
    for i in arr:
        templist.append(i[k])
    indexlist=[]
    for e in range(len(templist)):
        indexlist.append(templist.index(max(templist)))
        templist[templist.index(max(templist))]=-1
    indexlist.reverse()
    if k!=1:
        for i in indexlist:
            k=arr[i]
            strk=str()
            for item in k:
                strk=strk+str(item)+" "
            print strk
