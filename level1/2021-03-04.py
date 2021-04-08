# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    answer = ''
    i = len(s) // 2
    
    if len(s) % 2:
        answer = s[i]
    else:
        answer = s[i-1] + s[i]
    
    return answer