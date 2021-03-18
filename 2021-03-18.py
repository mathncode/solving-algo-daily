# https://programmers.co.kr/learn/courses/30/lessons/12930
# 이상한 문자 만들기

def solution(s):
    capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    capital_idx = []    # 문자열 중에 대문자만 골라 해당 인덱스 담을 리스트    
    
    for i in range(len(s)): # 문자열 중 대문자만 골라 인덱스를 기록
        if 65 <= ord(s[i]) <= 90:
            capital_idx.append(i)

    c, j = 0, 0
    for i in range(len(s)):
        j = i - c   # j는 공백이 나올 때마다 c를 빼서 공백 다음 문자가 0번 인덱스가 되게 함
        
        if s[i] == ' ':
            answer += s[i]
            c = (i + 1)
            continue

        if j % 2:
            if i in capital_idx: 
                idx = capital.find(s[i])
                answer += small[idx]
            else: answer += s[i]    
        else:
            if i not in capital_idx: 
                idx = small.find(s[i])
                answer += capital[idx]
            else: answer += s[i]              
    
    return answer