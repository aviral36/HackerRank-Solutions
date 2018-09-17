import math

def p(x):
    e = math.e
    f = math.factorial(x)
    prob = (pow(e,-2.5)*pow(2.5,x))/f
    return prob
mean = 2.5
l = 2.5
# we know that mean=lambda
#p(x) = (e^-lambda)*lambda^x/(x!)

x = 5
prob = p(x)
print(round(prob,3))
