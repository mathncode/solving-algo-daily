# https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    answer = True
    
    s = s.lower()
    count_p, count_y = 0, 0
    
    for i in s:
        if i == 'p':
            count_p += 1
        if i == 'y':
            count_y += 1
    
    if count_p != count_y:
        answer = False
        
    return answer