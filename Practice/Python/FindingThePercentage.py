import math
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for i in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    if student_marks.has_key(query_name)==True:
        q=student_marks[query_name]
        sum=0
        for i in q:
            sum=sum+i
        avg=sum/len(q)
        print "%.2f" %avg
        
            
        
