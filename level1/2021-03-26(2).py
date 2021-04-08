# https://programmers.co.kr/learn/courses/30/lessons/12940
# 최대 공약수와 최소공배수

import math
def solution(n, m):
    g = math.gcd(n, m)
    l = m * n // g      # m * n = g * l
    
    return [g, l]

# 증명 : 두 수 a, b와 최대공약수 g라 하면 a = gm, b = gn (m, n 서로소)
# a, b의 최소공배수 l은 l = gmn 이므로 ab = gmgn = ggmn = gl 이다.     