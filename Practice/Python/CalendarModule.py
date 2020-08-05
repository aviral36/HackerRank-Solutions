import calendar
n=raw_input()
a=n.split(" ")
month=int(a[0])
date=int(a[1])
year=int(a[2])
day=calendar.weekday(year,month,date)
if day==0:
    print 'MONDAY'
elif day==1:
    print 'TUESDAY'
elif day==2:
    print 'WEDNESDAY'
elif day==3:
    print 'THURSDAY'
elif day==4:
    print 'FRIDAY'
elif day==5:
    print 'SATURDAY'
elif day==6:
    print 'SUNDAY'    
