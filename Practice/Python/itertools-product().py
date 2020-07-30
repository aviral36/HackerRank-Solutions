# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
A=list(map(int, raw_input().split()))
B=list(map(int, raw_input().split()))
A=list(product(A,B))
for i in A:
    print i,
