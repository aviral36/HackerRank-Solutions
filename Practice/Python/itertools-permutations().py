# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s=raw_input().split()
le=len(s[0])
l=list()
k=int(s[1])
for i in s[0]:
    l.append(i)
f=list(permutations(l,k))
f.sort()
for i in f:
    temp="".join(i)
    print temp
    
