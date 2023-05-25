def solution(n):
    answer = ''
    s = []
    for i in range(n):
        if i%2 == 0:
            s.append("수")
        elif i%2 == 1:
            s.append("박")
    answer = ''.join(s)
    return answer