def merge_the_tools(string, k):
    l=list()
    for i in range(0,len(string),k):
        l.append(string[i:i+k])
    for i in range(len(l)):
        case=l[i]
        reg=str()
        for i in range(k):
            if case[i] not in reg:
                reg=reg+case[i]
        print reg
        
        
