def capitalize(string):
    l=list()
    for i in string:
        l.append(i)
    length=len(l)
    q=l[0].upper()
    l[0]=q
    for i in range(1,length+1):
        if l[i-1]==' ':
            a=l[i].upper()
            l[i]=a
    strout=str()
    for i in range(length):
        strout=strout+l[i]
    return strout
        
            

