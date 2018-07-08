T = int(input())
for _ in range(T):
    s = input()
    l = len(s)
    eve = str()
    odd = str()
    for i in range(l):
        if i%2==0:
            odd = odd+s[i]
        else:
            eve = eve+s[i]
    print(odd, eve)
