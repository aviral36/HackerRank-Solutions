# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
s=raw_input().split()
k=int(s[1])
l=list()
for i in s[0]:
    l.append(i)
l.sort()
string="".join(l)
temp=list(combinations_with_replacement(string,k))
temp.sort()
for q in temp:
    e="".join(q)
    print e
