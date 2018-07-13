import math

def calcmean(a,n):
    add = 0.0
    for i in a:
        add = add+i
    mean = round(add/n,1)
    print(mean)

def calcmedian(a,n):
    if n%2 != 0:
        median = a[math.ceil(n/2)-1]
    else:
        median = (a[int(n/2)]+a[int(n/2)-1])/2
    print(round(median,1))
    
def calcmode(a,n):
    s = set(a)
    arr=[]
    for i in s:
        arr.append(a.count(i))
    m = max(arr)
    t=list(s)
    if arr.count(m) == 1:
        mode = t[arr.index(m)]
        print(round(mode,1))
    else:
        newarr=[]
        we = len(arr)
        for x in range(we):
            if arr[x]==m:
                newarr.append(t[x])
        print(round(min(newarr),2))  

y = int(input())
a = map(float,list(input().split()))
p = list(a)
p.sort()
n=len(p)
calcmean(p,n)
calcmedian(p,n)
calcmode(p,n)
