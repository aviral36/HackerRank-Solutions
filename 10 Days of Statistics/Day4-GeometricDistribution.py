def prob(x,p,q):
    s = pow(p,1)*pow(q,x-1)
    return s   
    
p = 1/3
x = 5
q = 2/3
probability = prob(x,p,q)
print(round(probability,3))
