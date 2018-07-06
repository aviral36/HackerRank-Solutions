mport math
T=int(input())
for a0 in range(T):
    N=int(input())
    f=math.factorial(N)
    s=str(f)
    sum=0
    for i in s:
        sum=sum+int(i)
    print(sum)
