# Enter your code here. Read input from STDIN. Print output to STDOUT
str_in=raw_input()
alpha_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
count=0
for i in range(26):
    if alpha_list[i] in str_in.lower():
        count=count+1
if count==26:
    print 'pangram'
else:
    print 'not pangram'
