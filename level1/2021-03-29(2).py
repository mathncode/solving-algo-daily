# https://programmers.co.kr/learn/courses/30/lessons/42889
# 실패율

def solution(N, stages):
    answer = []
    temp = []
    stages.sort()   # for문의 연산 횟수 줄이기 위해 오름차순 정렬

    user = len(stages)  # 스테이지에 도달한 유저 수. 모든 유저는 1번 스테이지에 도달한 상태이다.
    lev = 1             # 스테이지 번호
    idx = 0             # for문의 시작 index
    while lev <= N:
        count = 0       # 스테이지에 도달했으나 클리어 못한 유저 수
        for i in range(idx, len(stages)):
            if stages[i] == lev:
                count += 1
            elif stages[i] > lev:
                idx = i
                break
        
        if user == 0:                         # 스테이지에 도달한 유저가 없는 경우 
            temp.append((lev, 0))
        else:    
            temp.append((lev, count / user))  # 실패율 계산
        
        user -= count
        lev += 1
    
    temp = sorted(temp, key= lambda x: x[1], reverse=True)  # 실패율이 높은 순으로 정렬
    
    for i in temp:              # 정렬된 temp에서 스테이지 번호만 새 list에 담기
        answer.append(i[0])
    
    return answer