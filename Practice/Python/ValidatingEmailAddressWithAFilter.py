def fun(s):
    temp='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_'
    tempo='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    if '@' not in s:
        return False
    else:
        k=s.split('@')
        username=k[0]
        if username=='':
            return False
        domain=k[1]
        for i in username:
            if i not in temp:
                return False
        if '.' not in domain:
            return False
        else:
            q=k[1].split('.')
            host=q[0]
            extension=q[1]
            if len(extension)>3:
                return False
            elif len(extension)==0:
                return False
            for i in host:
                if i not in tempo:
                    return False
            return True
        
