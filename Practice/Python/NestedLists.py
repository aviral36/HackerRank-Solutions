n=input()
l=list()
m=list()
k=list()
for i in range(n):
    q=list()
    a = raw_input()
    b = float(raw_input())
    q.append(a)
    q.append(b)
    l.append(q)
for i in range(n):
    m.append(l[i][1])
m.sort()
u=m[::-1]
min=m[0]
for i in m:
    if u[-1]==min:
        n=u.pop()
v=u[-1]
for i in range(len(l)):
    if l[i][1]==v:
        k.append(l[i][0])
k.sort()
for i in k:
    print i
