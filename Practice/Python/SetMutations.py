# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()                 #size of s
s = set(map(int, raw_input().split()))
N=input()                   #number of sets
for i in range(N):
    comm=(raw_input()).split()
    s2 = set(map(int, raw_input().split()))
    if comm[0]=='intersection_update':
        s.intersection_update(s2)
    elif comm[0]=='update':
        s.update(s2)
    elif comm[0]=='symmetric_difference_update':
        s.symmetric_difference_update(s2)
    elif comm[0]=='difference_update':
        s.difference_update(s2)
print sum(s)
    
