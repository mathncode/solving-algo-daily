# https://programmers.co.kr/learn/courses/30/lessons/12915

# 테스트 스트링 = ['bbce', 'abce', 'abcd', 'cdf', 'zeb', 'bdg','aeg']

def solution(strings, n):
    arr = sorted(strings)   # ['abcd', 'abce', 'aeg', 'bbce', 'bdg', 'cdf', 'zeb']
    answer = sorted(arr, key = lambda x: x[n])  # ['zeb', 'abcd', 'abce', 'bbce', 'cdf', 'aeg', 'bdg']



# 꼭 문제 지문의 순서대로 코드를 구성할 필요가 없다면, 순서를 거꾸로 구성해보는 것도 좋을 듯하다.