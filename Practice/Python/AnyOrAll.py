N=input()
l=map(int,raw_input().split())
l.sort()
flag=0

if l[0]<0:
    print 'False'
else:
    for i in l:
        if str(i)==str(i)[::-1]:
            flag=flag+1
    if flag>=1:
        print 'True'
    else:
        print 'False'
