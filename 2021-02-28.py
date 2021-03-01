# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    student = [1]*n
    student.append(1)
    student.append(1)
    count = 0
    
    for i in reserve:
        student[i] = 2
    
    for i in lost:
        student[i] -= 1 
    
    for i in range(1, n+1):
        if student[i] == 2 and student[i-1] == 0:
            student[i] = 1
            student[i-1] = 1
        elif student[i] == 2 and student[i+1] == 0:    
            student[i] = 1
            student[i+1] = 1
    
    count = student.count(0)
    answer = n - count
    
    return answer