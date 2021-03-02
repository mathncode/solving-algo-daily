# https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    answer = ''
    
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    day = 0

    for i in range(a):
        day += month[i]
    day += b

    ind = (day - 1) % 7  

    answer = day_of_week[ind]
    
    return answer