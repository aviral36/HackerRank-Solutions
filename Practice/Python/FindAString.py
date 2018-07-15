def count_substring(s, a):
    l=len(s)
    p=len(a)
    count=0
    for i in range(l):
        if s[i]==a[0]:
            if s[i:i+p]==a:
                count=count+1
    return count
