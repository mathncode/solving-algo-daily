# https://programmers.co.kr/learn/courses/30/lessons/17682
# 다트 게임

def solution(dartResult):
    score = [0, 0, 0]
    ops = [None, None, None]    # 옵션
    exp = -1    # 보너스 위치 0, 1, 2
    n = -1      # 점수 위치 0, 1, 2
   
    for i in dartResult:
        if i in '123456789':    
            n += 1              # 점수 인식  
            score[n] = int(i)
        elif i == '0':
            if n > exp:         # 보너스 인식이 안됐는데 점수가 연속해서 인식되므로 10점
                score[n] = 10
            else:
                n += 1 
                score[n] = int(i)    

        if i in 'SDT':
            exp += 1            # 보너스 인식 
            if i == 'D':
                score[n] = score[n] ** 2    
            elif i == 'T':
                score[n] = score[n] ** 3

        if i in '*#':           # 옵션은 나중에 연산하기 위해 위치에 맞게 옵션 저장
            ops[n] = i       
            
    for i in range(3):          # 옵션에 맞게 score를 추가 연산
        if ops[i] == '*':
            if i == 0:
                score[i] *= 2
            else:
                score[i - 1] *= 2    
                score[i] *= 2
        if ops[i] == '#':
            score[i] *= -1
    
    answer = sum(score)
    return answer

# 10을 처리할 때,
# 현재 풀이 처럼 체크할 수 있는 별도의 문자 마련
# 바로 직전에 인식했던 문자를 계속 한 문자에 저장해서 현재 문자와 확인
# 처음부터 주어진 문자열에서 10을 A로 치환해서 '0123456789A' 로 처리
# 정규표현식의 사용      