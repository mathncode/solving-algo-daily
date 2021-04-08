# https://programmers.co.kr/learn/courses/30/lessons/17681
# 비밀지도

def solution(n, arr1, arr2):
    # 배열의 수를 비트연산(OR)
    def card_conv(a1, a2):
        temp = []
        for i in range(len(a1)):
            temp.append(bin(a1[i] | a2[i]))
        return temp
    
    arr = card_conv(arr1, arr2)
    
    answer = []
    for pw in arr:
        # OR 연산 결과를 가져와 0과 1을 ' '과 '#'으로 변환
        t = ''
        if len(pw) < n + 2:     # OR 연산 결과가 n자리가 안되면 부족한 자릿수만큼 ' '추가
            for _ in range(n + 2 - len(pw)):
                t += ' ' 
        for i in range(2, len(pw)): # pw는 0b11111 같은 형태의 문자열이므로 3번째 원소부터 가져온다.
            if pw[i] == '1':
                t += '#'
            else:
                t += ' '
        answer.append(t)
    
    return answer