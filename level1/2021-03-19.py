# https://programmers.co.kr/learn/courses/30/lessons/12931
# 자릿수 더하기

# n은 10진수이므로 10으로 나눌 때마다 자릿수가 나오는 것을 이용합니다. 
def solution(n): 
    sum_of_digit = 0    # 자릿수 합
    while n > 0:
        sum_of_digit += n % 10  # n % 10은 자릿수, 1의 자리부터 역으로 구해서 더하기
        n //= 10
    return sum_of_digit