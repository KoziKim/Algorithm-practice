import sys
input = sys.stdin.readline
N = int(input())
feat = list(map(int, input().split()))
feat.sort()
ans = []

left = 0
right = N-1
target = 2e9 + 1

while left < right:
    total = feat[right] + feat[left]
    if abs(total) < target:
        target = abs(total)
        ans = [feat[left], feat[right]]
    if feat[right] + feat[left] < 0:
        left += 1
    else:
        right -= 1

print(ans[0], ans[1])