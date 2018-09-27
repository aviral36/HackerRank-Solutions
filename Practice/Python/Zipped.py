# Enter your code here. Read input from STDIN. Print output to STDOUT
l=map(int,raw_input().split())
N=l[0]
X=l[1]
li=[]
for i in range(X):
    t=map(float, raw_input().split())
    li.append(t)
sumli=zip(*li)
for part in sumli:
    average=sum(part)/X
    print average
        
