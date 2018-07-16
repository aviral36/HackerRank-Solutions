# Enter your code here. Read input from STDIN. Print output to STDOUT
en=input()
arr1=map(int,((raw_input()).split()))
fr=input()
arr2=map(int,((raw_input()).split()))
english=set(arr1)
french=set(arr2)
r=english.intersection(french)
print len(r)
