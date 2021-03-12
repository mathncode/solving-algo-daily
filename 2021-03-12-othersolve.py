# https://programmers.co.kr/learn/courses/30/lessons/12921
# 소수 찾기

# 에라토스테네스의 체 알고리즘
def solution(n):
    answer = 0
    array = [True for i in range(n+1)]  

    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:  
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    for i in range(2, n + 1):
        if array[i]:
            answer += 1 
    
    return answer

# 내 기존 풀이보다 약 3.7배 빠르다. 대신 메모리 5MB 정도 더 사용.    