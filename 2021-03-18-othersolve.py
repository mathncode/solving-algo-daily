def solution(inp):
    pp=[]
    for s in inp.split(' '):
        ss=[]
        for i in range(len(s)):
            if i%2==0:
                ss.append( s[i].upper())    # 한 글자도 문자열 함수를 적용할 수 있다.
            else:
                ss.append(s[i].lower())
        pp.append(('').join(ss))
    return (' ').join(pp)

def solution1(inp):
    return (' ').join([''.join([s[i].upper() if i%2==0 else s[i].lower() for i in range(len(s))]) for s in inp.split(' ')])

example = "try hello world"
print(solution1(example)) #'TrY HeLlO WoRlD'