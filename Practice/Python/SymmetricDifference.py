# Enter your code here. Read input from STDIN. Print output to STDOUT
m=input()
arr1=raw_input()
arrm=arr1.split()
arrM=list(map(int,arrm))
n=input()
arr2=raw_input()
arrn=arr2.split()
arrN=list(map(int,arrn))
setm=set(arrM)
setn=set(arrN)
ln=list(setn)
lm=list(setm)
new=list()
for i in lm:
    if i not in ln:
        new.append(i)
for i in ln:
    if i not in lm:
        if i not in new:
            new.append(i)
new.sort()
for i in new:
    print i
