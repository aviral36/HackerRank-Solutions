cube = lambda x: pow(x,3)
def fibonacci(n):   
    l=list()
    if n==0:
        l=[]
    elif n==1:
        l=[0]
    else:
        l=[0,1]
        for i in range(2,n):
            num=l[i-1]+l[i-2]
            l.append(num)
    return 1
