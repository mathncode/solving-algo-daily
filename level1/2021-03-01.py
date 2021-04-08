# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    
    for a in range(len(commands)):
        c_arr = commands[a]

        arr = array[c_arr[0]-1 : c_arr[1]]
        arr.sort()

        r = arr[c_arr[2]-1]
        answer.append(r)
            
    return answer