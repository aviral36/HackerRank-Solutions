import math
def calcmean(X,N):
    sum = 0
    for i in range(N):
        sum = sum+X[i]
    mean = float(sum/N)
    return mean
    
N = int(input())
X = list(map(int,list(input().split())))

u = calcmean(X,N)
net = 0.0
for xi in X:
    net = net + pow(xi-u,2)
var = float(net/N)
stdev = math.sqrt(var)
print(round(stdev,1))
