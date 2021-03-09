# https://programmers.co.kr/learn/courses/30/lessons/12904

def solution(s):
    ind_odd = []   # 홀수 길이 부분 문자열의 중심 인덱스
    ind_even = []   # 짝수 길이 부분 문자열의 중심 인덱스
    sub_len_list = [0]  # 각 부분 문자열 최대 길이
    
    
    if len(s) == 1:
        ind_odd.append(0)    
    else:   # 부분 문자열 중심 인덱스 찾아 담기
        if s[0] == s[1]: ind_even.append(0)
        for i in range(1, len(s)-1):
            if s[i] == s[i+1]: ind_even.append(i)
            if s[i-1] == s[i+1]: ind_odd.append(i)
        
    count = 0
    for i in range(len(ind_odd)):   # 홀수 길이 문자열 최대 길이 구하기
        for j in range(0, min(ind_odd[i], len(s) - ind_odd[i] - 1)):
            if s[ind_odd[i]-1-j] != s[ind_odd[i]+1+j]: break
            else: count += 1
        sub_len_list.append(count*2 + 1)
        count = 0

    for i in range(len(ind_even)):  # 짝수 길이 문자열 최대 길이 구하기
        for j in range(0, min(ind_even[i] + 1, len(s) - ind_even[i] -1)):
            if s[ind_even[i]-j] != s[ind_even[i]+1+j]: break
            else: count += 1
        sub_len_list.append(count*2)
        count = 0


    answer = max(sub_len_list)  # 부분 문자열 중 최대 길이 구하기
    return answer

# 테스트 케이스: "abcdcba", "abacde", "cdaade", "abcdcbajklml", "zxxzabcdcbajklmlcdaad", "a"    