# 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921

# n의 제곱근보다 작은 소수들로만 n을 나누어서 나누어 떨어지는게 없으면 n은 소수. 
import math

def solution(n):
    sr_list = []
    
    for i in range(2, n + 1):
        flag = True
        square_root = math.sqrt(i)
        
        for j in sr_list:
            if j > square_root: break
            
            # n의 제곱근 보다 작은 소수 중 한 소수에 의해 나누어 떨어지면 아래 if문에서 i가 list에 들어가지 않게 함.
            if i % j == 0:   
                flag = False
                break
           
        if flag: sr_list.append(i)
          
    answer = len(sr_list)
    return answer