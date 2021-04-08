# https://programmers.co.kr/learn/courses/30/lessons/12928
# 약수의 합
# 사용 수학 알고리즘: 24 = 2^3 * 3 으로 소인수 분해. 양의 약수 합은 (1 + 2 + 2^2 + 2^3)(1 + 3) = 60 

import math

def solution(n):
    if n == 0: return 0 # n = 0 일때, 0은 모든 자연수의 배수이므로 문제 오류 입니다. 답을 맞추기 위해 사용.

    prime = [2, 3]  # n보다 작은 소수를 담는 리스트
    
    for i in range(5, n + 1, 2):    # 2이상의 소수는 모두 홀수
        flag = True
        square_root = math.sqrt(i)

        for j in prime: # i의 제곱근 보다 작은 소수에 대해서만 확인
            if j > square_root: break
            if i % j == 0:   
                flag = False
                break

        if flag and n % i == 0: prime.append(i) # n을 나누는 소수만 prime에 담는다.
    
    # 소인수 분해 후 양의 약수의 합 구하는 알고리즘 구현. 두번의 for문 사용.
    temp = []    
    for i in prime:     # 각 소인수 마다 제곱수의 부분합을 구합니다. 
        k = n
        part_sum = 1    
        j = 1
        while k % i == 0:
            part_sum += i ** j
            j += 1
            k //= i
        if s != 1:
            temp.append(part_sum)
    
    answer = 1
    for i in temp:      # 구해진 부분합 끼리 곱합니다.
        answer *= i 
    
    return answer