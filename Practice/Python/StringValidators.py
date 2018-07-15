s = raw_input()
n1=0
n2=0
n3=0
n4=0
n5=0
for i in s:
    if i.isalnum():
        n1=n1+1
for i in s:
    if i.isalpha():
        n2=n2+1  
for i in s:
    if i.isdigit():
        n3=n3+1
for i in s:
    if i.islower():
        n4=n4+1
for i in s:
    if i.isupper():
        n5=n5+1
if n1==0:
    print "False"
else:
    print "True"
if n2==0:
    print "False"
else:
    print "True"
if n3==0:
    print "False"
else:
    print "True"
if n4==0:
    print "False"
else:
    print "True"
if n5==0:
    print "False"
else:
    print "True"
