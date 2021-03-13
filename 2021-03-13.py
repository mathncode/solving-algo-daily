# https://programmers.co.kr/learn/courses/30/lessons/12922
# 수박수박수박수?

def solution(n):
    str = '수박'
    
    if n % 2:
        answer = str * ((n-1)//2) + '수'
    else:
        answer = str * (n//2)
        
    return answer