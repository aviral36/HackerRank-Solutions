# Enter your code here. Read input from STDIN. Print output to STDOUT
k=input()
l = map(int, raw_input().split())
#s=filter(lambda i: l.count(i)==1,l)
#print s[0]
s=set(l)
for i in s:
    e=l.index(i)
    del l[e]
    if i not in l:
        print i
        break
    

        
    


