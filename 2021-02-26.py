# https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    #1 소문자화
    id = new_id.lower()
    
    #2 문자제거
    p_char = '0123456789abcdefghijklmnopqrstuvwxyz-_.'
    per = list(p_char)
    remove_set = []

    for i in id:
        if i not in per:
            remove_set.append(i)

    remove_set = set(remove_set)
    id = [i for i in id if i not in remove_set]
    
    #3 '.' 중복 제거
    for i in range(len(id)-1):
        if id[i] == '.' and id[i+1] =='.':
            id[i] = ''
    id = ''.join(id)  
    
    #4 첫끝 마침표 제거
    id = list(id)
    if id[0] == '.': id[0] = ''
    if id[-1] == '.': id[-1] =''
    id = ''.join(id)
    
    #5 id가 빈 문자열이라면, "a" 대입
    if id == '': id = 'a'
        
    #6 id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    # 만약 제거 후 마침표(.)가 id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다. 
    if len(id) > 15: 
        id = id[0 : 15]
        if id[14] == '.': id = id[0 : 14]    
    
    #7 id의 길이가 2자 이하라면, id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    id = list(id)
    if len(id) <= 2:
        ins = id[-1]
        while len(id) < 3:
            id.append(ins)
    
    answer = ''.join(id)
    return answer