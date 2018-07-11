n = int(input())
x = list(map(float, list(input().split())))
w = list(map(float, list(input().split())))
sumw = 0
add = 0
for i in range(n):
    add = add+(x[i]*w[i])
    sumw = sumw+w[i]
mean = add/sumw
print(round(mean,1))
