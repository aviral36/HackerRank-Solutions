if __name__ == '__main__':
    import math
    N = int(raw_input())
    l=list() 
    for i in range(N):
        w=raw_input().split(" ")
        if w[0]=='insert':
            l.insert(int(w[1]),int(w[2]))
        if w[0]=='print':
            print l
        if w[0]=='pop':
            l.pop()
        if w[0]=='remove':
            l.remove(int(w[1]))
        if w[0]=='append':
            l.append(int(w[1]))
        if w[0]=='sort':
            l.sort()
        if w[0]=='reverse':
            l.reverse()
