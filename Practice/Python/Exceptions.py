T = int(input())
for o in range(T):
    [a,b] = map(str,list(input().split()))
    try:
        q = int(a)
        e = int(b)
        print(int(q/e))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as v:
        print("Error Code:", v)
