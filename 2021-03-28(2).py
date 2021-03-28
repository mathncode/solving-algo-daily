# https://programmers.co.kr/learn/courses/30/lessons/12982
# 예산

# 최대 몇 개의 부서에 지원 가능한지는 최소 예산부터 차례로 더할 때 구할 수 있다.
import heapq

def solution(d, budget):
    t = []
    for i in d:
        heapq.heappush(t, i)
 
    s = 0
    j = 0
    while j < len(d):
        s += heapq.heappop(t)
        if s > budget:
            break
        j += 1    
    
    return j