def is_leap(year):
    leap = False
    if (year%4)==0 & (year/4)%2==0:
        if(year%100)==0 & (year/100)%2==0:
            if(year)%400==0 & (year/400)%2==0:
                leap=True
            else:
                leap=False
        else:
            leap=True     
    else:
        leap=False
    
    return leap
