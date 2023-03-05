import sys

input = sys.stdin.readline
global n
n = 0
ans = []
N = int(input())

def hanoi(N, S, E, M):
    if N > 20:
        print(2**N-1)
        return
    global n
    n += 1
    if N == 1:
        ans.append(f"{S} {E}")
        return
    else:
        hanoi(N-1, S, M, E)
        ans.append(f"{S} {E}")
        hanoi(N-1, M, E, S)

hanoi(N, 1, 3, 2)
if N <= 20:
    print(n)
for i in range(n):
    print(ans[i])