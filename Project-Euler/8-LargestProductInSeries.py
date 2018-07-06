#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    roles=[]
    for i in range(n-k+1):
        test=str(num)[i:i+k]
        if '0' not in test:
            roles.append(test)
    if len(roles)==0:
        print(0)
    products=[]
    length=len(roles)
    for x in range(length):
        n1=roles[x]
        prod=1
        for dig in range(k):
            prod=prod*int(n1[dig])
            products.append(prod)
    print(max(products))
        
