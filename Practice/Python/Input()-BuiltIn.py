# Enter your code here. Read input from STDIN. Print output to STDOUT
l=map(int,raw_input().split())
x=l[0]
k=l[1]
p=input()
e=str(p)
val=eval(e.replace('x',str(x)))
if val==k:
    print 'True'
else:
    print 'False'
