# https://programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
    answer = '김서방은 ' + str(seoul.index('Kim')) + '에 있다'
    
    # iterable.index() iterable에서 내가 찾는 data의 index 리턴. 단, set 안됨
    
    #for i in range(len(seoul)):
    #    if seoul[i] == 'Kim':
    #        answer = '김서방은 ' +str(i)+'에 있다'
    return answer