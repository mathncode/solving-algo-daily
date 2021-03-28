# https://programmers.co.kr/learn/courses/30/lessons/12954
# x만큼 간격이 있는 n개 숫자

def solution(x, n):
    # 등차수열의 첫항 a, 공차 d일 때 일반항은 a_n = a + (n-1)d 이다.
    return [x + i * x for i in range(n)]