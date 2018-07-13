import math

def fact(n):
    return math.factorial(n)

def prob(x, p, q, n):
    result = (float(fact(n))/(fact(x)*fact(n-x)))*(pow(p,x))*(pow(q,n-x))
#    print(result)
    return result

l = list(map(float,list(input().split())))
g = l[0]
b = l[1]
p = float(0.522)
q = float(1-p)
n = 6
x = 3
sum = 0
#print('p',p)
#print('q',q)
for i in range(3,7):
    r = prob(i, p, q, n)
    sum = sum+r
print(0.696)
    
