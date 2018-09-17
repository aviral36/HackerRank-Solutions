def prob(x,p,q):
    sum = 0
    for i in range(x):
        sum = sum + p*pow(q,i)
    return sum   
    
p = 1/3
x = 5
q = 2/3
probability = prob(x,p,q)
print(round(probability,3))
