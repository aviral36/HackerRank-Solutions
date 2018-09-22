import numpy
N,M=map(int,input().split())
A=[]
B=[]
for i in range(N):
    row=list(map(int,input().split()))
    A.append(row)
for j in range(N):
    row1=list(map(int,input().split()))
    B.append(row1)    
arrA=numpy.array(A, int)
arrB=numpy.array(B,int)
print(arrA+arrB)
print(arrA-arrB)
print(arrA*arrB)
div = arrA//arrB
print(div)
print(arrA%arrB)
print(arrA**arrB)
