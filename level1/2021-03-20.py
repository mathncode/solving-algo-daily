# https://programmers.co.kr/learn/courses/30/lessons/12932
# 자연수 뒤집어 배열로 만들기

def solution(n):
    answer = []
    while n > 0:
        answer.append(n % 10)
        n //= 10
    return answer