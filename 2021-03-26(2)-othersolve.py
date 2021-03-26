# https://programmers.co.kr/learn/courses/30/lessons/12940
# 최대 공약수와 최소공배수

# math 모듈의 gcd()를 사용하면 재미 없으니 유클리드 알고리즘을 이용해서 최대공약수 구해보자.
def solution(n, m):
    # g: 최대공약수, l: 최소공배수
    a = max(m, n)
    b = min(m, n)
    g = 0
    while True:
        r = a % b
    
        if r != 0:
            a = b
            b = r  
        else:
            g = b
            break
    
    l = m * n // g  
    return [g, l]


# 유클리드 :  피제수를 제수로 나눈 나머지 있을 때 제수가 피제수로, 나머지가 제수가 되는 과정을 반복. 
#            나머지가 0이면 그때의 제수가 최대공약수.

# 예로 설명하면 12, 30에 대해,
# 30 = 12*2 + 6  ->  12 = 6*2 + 0  나머지가 0이므로 제수인 6이 최대공약수.