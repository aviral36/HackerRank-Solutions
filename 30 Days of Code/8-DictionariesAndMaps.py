n = int(input())
phonebook=dict()
for _ in range(n):
    q = list(map(str,list(input().split())))
    name = q[0]
    phone = int(q[1])
    phonebook[name]=phone
try:
    while True:
        query = input()
        if query!="":
            if query in phonebook:
                st = query+'='+str(phonebook[query])
                print(st)
            else:
                print('Not found')
        else:
            break
except EOFError:
    pass
            
