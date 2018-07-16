n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    S = list(map(str, list(input().split())))
    if S[0] == 'pop':
        s.pop()
    elif S[0] == 'discard':
        s.discard(int(S[1]))
    else:
        s.remove(int(S[1]))
print(sum(list(s)))
