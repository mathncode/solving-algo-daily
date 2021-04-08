# https://programmers.co.kr/learn/courses/30/lessons/12926
# 시저 암호
def solution(s, n):
    capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
        elif s[i] in capital:
            ind = capital.find(s[i])
            answer += capital[(ind + n) % 26]
        else:
            ind = small.find(s[i])
            answer += small[(ind + n) % 26]
        
    return answer