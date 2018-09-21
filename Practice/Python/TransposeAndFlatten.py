import numpy
import sys

n,m = map(int, input().split())
lis=[]
for i in range(n):
    row=list(map(int,input().split()))
    lis.append(row)
arr=numpy.array(lis)
print(arr.transpose())
print(arr.flatten())
