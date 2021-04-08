# https://programmers.co.kr/learn/courses/30/lessons/12950
# 행렬의 덧셈

# 두 리스트에서 원소를 각각 하나씩 지정해서 덧셈. 한 행씩 처리.
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        t = []
        for j in range(len(arr1[i])):
            t.append(arr1[i][j] + arr2[i][j]) 
        answer.append(t)
    return answer


# zip()을 이용해서 두 list의 원소를 각각 하나 씩 가져와 처리. 위 방법보다 약간 더 빠르다.
def solution1(arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        t = []
        for a, b in zip(i, j):
            t.append(a + b) 
        answer.append(t)
    return answer


# 리스트 컴프리헨션으로 코드 줄이기
def solution2(arr1, arr2): 
    return [[a + b for a, b in zip(i, j)]for i, j in zip(arr1, arr2)]         