# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s=raw_input().split()
k=int(s[1])
l=list()
for i in s[0]:
    l.append(i)
l.sort()
string="".join(l)
for index in range(1,k+1):
    temp=list(combinations(string,index))
    temp.sort()
    for q in temp:
        e="".join(q)
        print e
