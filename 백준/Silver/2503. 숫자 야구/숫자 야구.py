import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input())
rounds = [list(map(int, input().split())) for i in range(N)]

def check(x, y, z):
    for round in rounds:
        question, strike, ball = str(round[0]), round[1], round[2]
        scnt = 0
        #질문과 같은 위치 숫자 같으면 스트라이크 1 추가
        if question[0] == x:
            scnt += 1
        if question[1] == y:
            scnt += 1
        if question[2] == z:
            scnt += 1
        #스트라이크 숫자랑 비교해서 다르면 False
        if scnt != strike:
            return False
        
        bcnt = 0
        #질문에 숫자 있지만 위치 다르면 볼카운트 1 추가
        if x in question and x != question[0]:
            bcnt += 1
        if y in question and y != question[1]:
            bcnt += 1
        if z in question and z != question[2]:
            bcnt += 1
        #볼 숫자랑 비교해서 다르면 False
        if bcnt != ball:
            return False
        #다 통과하면 True
    return True

# 999까지 돌면서 중복일때는 continue로 건너뛰기
# 해당 xyz가 모든 check 통과하면 가능한 숫자
# 가능한 숫자일때마다 1 추가.
ans = 0
for x in range(1, 10):
    for y in range(1, 10):
        if y == x:
            continue
        for z in range(1, 10):
            if x == z or y == z:
                continue
            if check(str(x), str(y), str(z)):
                ans += 1

print(ans)