def findmedian(x,n):
    if n%2 == 0:
        median = ((x[int(n/2)]+ x[int(n/2)-1])/2)
    else:
        median = x[int(n/2)]
    return median
        

n = int(input())
x = list(map(int,list(input().split())))
x.sort()
#print("x is", x)
median = findmedian(x,n)
if n%2 == 0:
    mid = int(n/2)-1
    x1 = x[:mid+1]
    l1 = len(x1)
    x2 = x[mid+1:]
    l2 = len(x2)
    median1 = findmedian(x1, l1)
    median2 = findmedian(x2, l2)
else:
    mid = int(n/2)
    x1 = x[:mid]
    x2 = x[mid+1:]
    l1 = len(x1)
    l2 = len(x2)
    median1 = findmedian(x1, l1)
    median2 = findmedian(x2, l2)
#print('x1=', x1)
#print('x2 =', x2)
print(int(median1))
print(int(median))
print(int(median2))
