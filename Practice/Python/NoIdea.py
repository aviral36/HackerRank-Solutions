# Enter your code here. Read input from STDIN. Print output to STDOUT
a=map(int, raw_input().split())
arr=map(int, raw_input().split())
A=set(map(int, raw_input().split()))
B=set(map(int, raw_input().split()))
happiness=0
for i in range(len(arr)):
    if arr[i] in A:
        happiness=happiness+1
    elif arr[i] in B:
        happiness=happiness-1
    else:
        happiness=happiness
print happiness
