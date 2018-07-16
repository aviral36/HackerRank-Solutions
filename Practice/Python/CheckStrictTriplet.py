A=set(map(int, raw_input().split()))
n=input()
count=0
for i in range(n):
    case=set(map(int, raw_input().split()))
    if A.intersection(case)==case:
        if A.intersection(case)!=A:
            count=count+1
if count==n:
    print 'True'
else:
    print 'False'
