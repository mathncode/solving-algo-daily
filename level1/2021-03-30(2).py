# https://programmers.co.kr/learn/courses/30/lessons/64061
# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    basket = []
    chk = -1            # basket의 마지막(상단) 인형번호
    for i in moves:
        i -= 1
        j = 0
        while j < len(board):
            if board[j][i] != 0:
                basket.append(board[j][i])
                board[j][i] = 0
                break
            j += 1
        else:
            continue            # 바닥까지 내려갔는데 인형이 없으므로 아무일도 없다.

        if chk == basket[-1]:   # 지금 바구니에 담는 인형번호와 바구니 상단 인형번호 비교
            basket.pop()
            basket.pop()
            answer += 2         # 터진 인형의 개수 추가

        if len(basket) == 0:    # 인형이 쌓였다가 모두 터져서 바구니가 비면 chk를 -1로 바꿈
            chk = -1
        else:
            chk = basket[-1]    # 그렇지 않으면 터진 후 가장 상단 원소를 chk로 바꾼다.
        
    return answer