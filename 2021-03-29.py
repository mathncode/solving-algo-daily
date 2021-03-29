# https://programmers.co.kr/learn/courses/30/lessons/68644
# 두 개 뽑아서 더하기

def solution(numbers):
    s = set()   # 집합은 중복도 순서도 없다.
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            s.add(numbers[i] + numbers[j])

    answer = sorted(list(s))
    return answer