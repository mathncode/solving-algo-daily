# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    
    #각 학생 찍는 패턴
    supo1p = [1, 2, 3, 4, 5]
    supo2p = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3p = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    #각 학생 맞힌 문제 개수
    supo1 = 0 
    supo2 = 0 
    supo3 = 0
    
    for i in range(len(answers)):
        if answers[i] == supo1p[i%5]: supo1 += 1
        if answers[i] == supo2p[i%8]: supo2 += 1
        if answers[i] == supo3p[i%10]: supo3 += 1


    # 높은 점수 받은 사람 찾기
    if supo1 == supo2 == supo3: answer = [1, 2, 3] #1=2=3
    elif supo3 > supo2 == supo1: answer = [3] #1=2<3
    elif supo3 < supo1 == supo2: answer = [1, 2] #3<1=2
    elif supo2 > supo3 == supo1: answer = [2] #1=3<2
    elif supo2 < supo1 == supo3: answer = [1, 3] #2<1=3
    elif supo1 > supo2 == supo3: answer = [1] #2=3<1
    elif supo1 < supo2 == supo3: answer = [2, 3] #1<2=3
    elif supo1 > supo2 > supo3: answer = [1] #3<2<1
    elif supo3 > supo1 > supo2: answer = [3] #1<2<3
    elif supo2 > supo1 > supo3: answer = [2] #3<1<2
    elif supo1 > supo3 > supo2: answer = [1] #2<3<1
    elif supo2 > supo3 > supo1: answer = [2] #1<3<2
    elif supo3 > supo2 > supo1: answer = [3] #1<2<3
    
    return answer