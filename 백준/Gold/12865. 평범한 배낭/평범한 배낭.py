import sys

inp = sys.stdin.readline

N, K = map(int, inp().split())
table = [0] * (K + 1)
for _ in range(N):
    w, v = map(int, inp().split())
    if w > K:
        continue
    for j in range(K, 0, -1):
        if j + w <= K and table[j] != 0:
            table[j+w] = max(table[j+w], table[j] + v)
    table[w] = max(table[w], v)
print(max(table))