# https://programmers.co.kr/learn/courses/30/lessons/1845#

def solution(nums):
    nums_set = set(nums)
    
    n = len(nums) / 2
    m = len(nums_set)
    
    if m > n:
        answer = n
    else:
        answer = m 
    
    return answer

# set() 이용하지 않으려면, set을 직접 구현해야 한다.
# 새 list를 만들고, if ~ not in을 이용해 중복 없게 새 list에 원소를 담으면 nums_set이 된다.     