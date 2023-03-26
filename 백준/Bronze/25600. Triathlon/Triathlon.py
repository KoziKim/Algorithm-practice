import sys
inp = sys.stdin.readline
n = int(inp().rstrip())

score = []
for i in range(n):
    a, d, g = map(int, input().split())
    if a == d+g:
        score.append(a*(d+g)*2)
    else:
        score.append(a*(d+g))
score.sort()
print(score[-1])
