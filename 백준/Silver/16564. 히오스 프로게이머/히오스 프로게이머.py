import sys
input = sys.stdin.readline

N, K = map(int, input().split())
levels = sorted([int(input()) for _ in range(N)])

l, r = min(levels), max(levels) + K

while l <= r:
    mid = (l + r) // 2
    total = 0
    for level in levels:
        if level >= mid:
            break
        total += mid - level
    if total <= K:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)