# https://programmers.co.kr/learn/courses/30/lessons/12915

# 테스트 문자열 리스트: strings = ['bbce', 'abce', 'abcd', 'cdf', 'zeb', 'bdg','aeg']

def solution(strings, n):
    answer = sorted(strings, key = lambda x: x[n])
    
    j, k = 0, 0  # 인덱스 n의 문자가 같은 문자열 여럿 일 경우, 시작(j)과 끝(k)을 가리키는 인덱스
    temp = []
    
    while j < len(answer)-1:
        for i in range(j, len(answer)-1):   # 시작 인덱스 뽑기
            if (answer[i])[n] == (answer[i+1])[n]:
                j = i
                break

        for i in range(j, len(answer)-1):   # 끝 인덱스 뽑기
            if (answer[i])[n] != (answer[i+1])[n]:
                k = i
                break
            if j > k: k = len(answer) - 1    
    
        for i in range(j, k+1):     # 시작-끝 부분만큼 추려서 temp에 담아 오름차순 정렬
            temp.append(answer[i])
        temp.sort()

        for i in range(len(temp)):  # temp의 원소를 answer에 끼워넣기
            answer[j + i] = temp[i]

        temp = []  # temp 초기화
        j = k + 1
    
    return answer