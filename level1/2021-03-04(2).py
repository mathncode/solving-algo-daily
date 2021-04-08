# https://programmers.co.kr/learn/courses/30/lessons/12906?language=python3

def solution(arr):
    answer = []
    front_value = -1
    
    for i in arr:
        if i != front_value:
            answer.append(i)
            front_value = i
    
    return answer