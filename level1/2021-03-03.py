# https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer = 0
    
    d = ''  # 변환된 3진수를 담을 빈 문자열, 3진수의 역순으로 담김
    base3 = '012'
    
    while n > 0:
        d += base3[n % 3]  # 해당하는 문자 꺼내 결합
        n //= 3

    m = len(d)

    for i in range(m):
        answer += int(d[i]) * pow(3, m - 1 -i)  # 10진수로 다시 변환
        
    return answer