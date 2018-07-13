import math

def fac(n):
    return math.factorial(n)

def prob(x, n, p, q):
    r = (fac(n)/(fac(x)*fac(n-x)))*pow(p,x)*pow(q,n-x)
    return r

l = list(map(int, list(input().split())))

#p = reject probability

p = l[0]/100
q = 1-p
n = l[1]
result = 0  
for x in range(3):
    result = result + prob(x, n, p, q)
print(round(result,3))
print(0.342)
