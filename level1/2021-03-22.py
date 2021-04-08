# https://programmers.co.kr/learn/courses/30/lessons/12934
# 정수 제곱근 판별

import math

def solution(n):
    sq_rt = math.sqrt(n)
    num = int(sq_rt)
    if sq_rt == num:
        return (num + 1) ** 2

    return -1