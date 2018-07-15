def print_formatted(number):
    spaces=len(format(number,'b'))
    for i in range(1,number+1):
        print str(i).rjust(spaces,' '), str(format(i,'o')).rjust(spaces,' '), str((format(i,'x').upper())).rjust(spaces,' '), str(format(i, 'b')).rjust(spaces,' ')  
