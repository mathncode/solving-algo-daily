# https://programmers.co.kr/learn/courses/30/lessons/12969
# 직사각형 별찍기

a, b = map(int, input().strip().split(' '))
# 반복문으로 해결
for _ in range(b):
    for _ in range(a):
        print('*', end='')
    print()

# 문자열 연산으로 해결
print(("*" * a + "\n") * b)          