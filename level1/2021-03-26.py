# https://programmers.co.kr/learn/courses/30/lessons/12912
# 두 정수 사이의 합

# 등차수열의 합 공식 이용. 
# 첫 항 a, 끝 항 b, 공차 1, 개수 n 일때, sum = 1/2 * (b-a) * (a+b)

def solution(a, b):
    m = max(a, b)                       # a, b 대소관계가 정해지지 않았으므로
    n = min(a, b)
    answer = (m - n + 1) * (m + n) // 2 # 공식 적용
    return answer  