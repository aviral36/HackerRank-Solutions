#!/bin/python
n=input();
if n%2!=0:
    print "Weird"
else:
    if 2<=n<=5:
        print "Not Weird"
    elif 6<=n<=20:
        print "Weird"
    elif 20<n<=100:
        print "Not Weird"
    else:
        print"try again"
