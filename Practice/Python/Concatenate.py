import numpy
n,m,p=map(int,input().split())
arr1=[]
arr2=[]
for i in range(n):
    row=list(map(int,input().split()))
    arr1.append(row)
array1=numpy.array(arr1)
for j in range(m):
    row1=list(map(int,input().split()))
    arr2.append(row1)
array2=numpy.array(arr2)
print(numpy.concatenate((array1, array2), axis=0))
