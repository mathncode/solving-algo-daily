# https://programmers.co.kr/learn/courses/30/lessons/12977
# 소수 만들기

import math
# 3개 숫자 중 홀수가 0개 또는 2개면 더한 값도 짝수. 짝수는 소수가 아니다.
def solution(nums):
    # 소수 판별
    def is_prime(x):
        for i in range(2, int(math.sqrt(x) + 1)):
            if x % i == 0:
                return False 
        return True 
    
    # 홀수 개수 확인 및 홀수, 짝수 구분
    count = 0
    odd_num = []
    even_num = []
    for i in nums:
        if i % 2:
            odd_num.append(i)
            count += 1
        else:
            even_num.append(i)    
    
    # nums의 모든 숫자가 짝수면, 숫자 3개 합이 소수가 될 수 없다.
    if count == 0: return 0    
    
    # 3개 원소 합 구하기
    temp = []
    for i in odd_num:   # 홀수 1개, 짝수 2개인 경우
        for j in range(len(even_num) - 1):
            for k in range(j + 1, len(even_num)):
                temp.append(i + even_num[j] + even_num[k])
    
    if count > 2:   # 홀수 3개인 경우
        for i in range(len(odd_num) - 2):
            for j in range(i + 1, len(odd_num) - 1):
                for k in range(j + 1, len(odd_num)):
                    temp.append(odd_num[i] + odd_num[j] + odd_num[k])

    # 3개 원소 합 중 소수 개수 구하기
    answer = 0
    for i in temp:
        if is_prime(i) == True:
            answer += 1
    
    return answer