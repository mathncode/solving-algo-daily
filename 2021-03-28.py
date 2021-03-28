# https://programmers.co.kr/learn/courses/30/lessons/12954
# x만큼 간격이 있는 n개 숫자

def solution(x, n):
    # 등차수열의 일반항: 첫항 a, 공차 d 일때 a_n = a + (n-1)d
    return [x + i * x for i in range(n)]