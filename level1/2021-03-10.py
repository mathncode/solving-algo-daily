# https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    answer = False
    l = len(s)
    check_str = '0123456789'
    
    if l == 4 or l == 6:
        answer = True
    
    for i in s:
        if i not in check_str:
            answer = False
    
    return answer


# 다른 사람 풀이
 # return s.isdigit() and len(s) in (4, 6)
 # return s.isdigit() and (len(s) == 4 or len(s) == 6) 