# https://programmers.co.kr/learn/courses/30/lessons/12935
# 제일 작은 수 제거하기

# 제한조건 중 '인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.'에 따라 index 집합과 value 집합이 일대일대응.
# 즉, 최솟값이 유일하게 존재한다는 것이다.
def solution(arr):
    min = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
            
    arr.remove(min)
    
    return arr if len(arr) > 0 else [-1]

# 다른 풀이. 모두 내장함수를 이용. 아래 풀이가 더 빠르다.
def solution1(arr):
    arr.remove(min(arr))
    
    return arr if len(arr) > 0 else [-1]   