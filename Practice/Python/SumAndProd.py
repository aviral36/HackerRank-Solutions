import numpy as np
NM=list(map(int,input().split()))
N=NM[0]
M=NM[1]
l=list()
for i in range(M):
    w = list(map(int,input().split()))
    l.append(w)
add = np.sum(l, axis=0)
print(np.prod(np.array(add)))
