# 영선이를 위해 이 정보들을 바탕으로 마지막으로 튀김 소보루를 집어 든 사람의 번호를 구하여라.

# 여러 사람이 동시에 소보루를 집는다면 번호가 작은 사람이 먼저 잡으며, 영선이가 떠나자 마자 바로 먹기를 시작한다.

# 예를 들어, 소보루를 먹는 시간이 1번은 1초, 2번은 3초, 3번은 5초에 하나씩 먹는다고 하고, 소보루는 1000개 있다고 하자.

# 1개가 줄었다면 1번 사람이 처음 빵을 집을 것이다.
# 2개가 줄었다면 2번 사람이 1번 사람이 집은 직후 처음 빵을 집을 것이다.
# 3개가 줄었다면 3번 사람이 2번 사람이 집은 직후 처음 빵을 집을 것이다.
# 4개가 줄었다면 1번 사람이 빵을 다 먹고, 2개째 빵을 집을 것이다.
# 5개가 줄었다면 1번 사람이 빵을 다 먹고, 3개째 빵을 집을 것이다.
# 6개가 줄었다면 1번 사람이 빵을 다 먹고, 4개째 빵을 집을 것이다.
# 7개가 줄었다면 2번 사람이 빵을 다 먹고 1번 사람이 집은 직후, 2개째 빵을 집을 것이다.
import sys
from math import lcm

n, s = map(int, input().split())

m = int(input())

t = []

cnt = 0

for i in range(m):
    t.append(int(sys.stdin.readline().rstrip()))

# print(lcm(*t))

lcm_t = lcm(*t)

yeah = 0
for i in range(m):
    yeah += lcm_t//t[i]
# print(yeah)

k = n-s

a = k//yeah

n -= a*yeah
# print(n)
# n += lcm(*t)
# print(n)

if n == s:
    print(m)

while n > s:
    for i in range(len(t)):
        if cnt%t[i] == 0:
            n -= 1
            # print("i",i, "cnt", cnt)
            # print("n", n)
        if n == s:
            print(i+1)
            break
    if n == s:
        break
    cnt += 1

