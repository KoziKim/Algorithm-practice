import sys

w, l = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
W = [0, w]
L = [0, l]
ans = 0

for i in range(N):
    sero, num = map(int, sys.stdin.readline().split())
    if sero:
        W.append(num)
    else:
        L.append(num)

W.sort()
L.sort()

for i in range(len(W) - 1):
    for j in range(len(L) - 1):
        ans = max(ans, (W[i+1] - W[i])*(L[j+1]-L[j]))

print(ans)