# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    p = sorted(participant)
    c = sorted(completion)
    
    answer = ''
    flag = False
    
    for i in range(len(c)):
        for j in range(i, len(p)):
            if p[i] == c[i]: break
            else:
                answer = p[i]
                flag = True
                break
        if flag:
            break  
    else: answer = p[-1]
        
    return answer