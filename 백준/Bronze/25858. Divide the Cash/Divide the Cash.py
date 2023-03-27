n, t = map(int, input().split())
num = 0
solve = [0] * n
for i in range(n):
    solve[i] = int(input())
    num += solve[i]
per = t // num
for i in range(n):
    print(per*solve[i])