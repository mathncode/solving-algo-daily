# https://programmers.co.kr/learn/courses/30/lessons/12933
# 정수 내림차순으로 배치하기
def solution(n):
    temp = []
    while n > 0:
        temp.append(n % 10)
        n //= 10
    temp.sort()
    
    answer = 0
    for i in range(len(temp)):
        answer += temp[i] * (10 ** i)
    return answer

# 다른 풀이. 효율은 위에 코드가 더 좋다.
def solution1(n):
    temp = []
    while n > 0:
        temp.append(str(n % 10))
        n //= 10
    temp.sort(reverse = True)
    answer = int(''.join(temp))
    return answer