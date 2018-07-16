# Enter your code here. Read input from STDIN. Print output to STDOUT
ne=input()
eng=map(int,(raw_input()).split())
nf=input()
fre=map(int,(raw_input()).split())
sete=set(eng)
setf=set(fre)
body=list(sete.union(setf))
print len(body)
