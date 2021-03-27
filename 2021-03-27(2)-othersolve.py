# https://programmers.co.kr/learn/courses/30/lessons/12977
# 소수 만들기

import math
from itertools import combinations
# 조합을 이용해서 3개 원소 합을 구한다. 
# 모든 경우를 검사하기 때문에 앞에 풀이보다 조금 느리다.
def solution(nums):
    # 소수 판별
    def is_prime(x):
        for i in range(2, int(math.sqrt(x) + 1)):
            if x % i == 0:
                return False 
        return True 
    
    # 홀수 개수 확인
    count = 0
    for i in nums:
        if i % 2:
            count += 1   
    
    # nums의 모든 숫자가 짝수면 계산할 필요 없다.
    if count == 0: return 0    
    
    # 서로 다른 3개 원소 뽑기 
    temp = list(combinations(nums, 3))
    
    # 3개 원소 합 구하기
    sum_of_3 = [sum(i) for i in temp]
    
    # 3개 원소 합 중 소수 개수 구하기
    answer = 0
    for i in sum_of_3:
        if is_prime(i) == True:
            answer += 1
    
    return answer