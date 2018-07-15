if __name__ == '__main__':
    n = int(raw_input())
    t=tuple()
    l = map(int, raw_input().split())
    t=tuple(l)
    print hash(t)
    
