# https://programmers.co.kr/learn/courses/30/lessons/67256
# [카카오 인턴] 키패드 누르기

# *, 0, #을 10, 11, 12로 생각하기
def solution(numbers, hand):
    def distance(a, b):
    """ 2, 5, 8, 0을 눌러야 할때 실행되는 거리 구하는 함수 """
        d = 0
        maxi = max(a, b)
        mini = min(a, b)
        
        if maxi != 0 and mini == 0: # 0을 11로 변환
            mini = maxi
            maxi = 11
    
        while maxi > 0:             # 거리 계산
            if maxi == mini:
                break
            if maxi - 1 == mini or maxi + 1 == mini:
                d += 1
                break
            maxi -= 3
            d += 1
        return d

    answer = ''
    left_f = [1, 4, 7]      # 무조건 왼손 엄지  
    right_f = [3, 6, 9]     # 무조건 오른손 엄지    

    lf, rf = 10, 12         # 현재 각 엄지 위치, 시작은 *, #이므로 10, 12로 둡니다.  

    for i in numbers:
        if i in left_f:     # 1, 4, 7이면 'L'을 추가 후 lf 업데이트
            answer += 'L'
            lf = i
        elif i in right_f:  # 3, 6, 9이면 'R'을 추가 후 rf 업데이트
            answer += 'R'    
            rf = i
        else:               # 2, 5, 8, 0면 i와 rf, i와 lf의 거리를 구한 후 비교해서 'R'이나 'L'추가
            ld = distance(i, lf)    
            rd = distance(i, rf)
            if ld > rd:
                answer += 'R'
                rf = i
            elif ld < rd:
                answer += 'L'
                lf = i
            else:   # 거리가 같으면 문제 조건에 따라 오른손잡이면 'R', 왼손잡이면 'L'
                if hand == 'right':
                    answer += 'R'
                    rf = i
                else:
                    answer += 'L'
                    lf = i 
    return answer