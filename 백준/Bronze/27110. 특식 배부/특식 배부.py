n = int(input())
soldier = list(map(int, input().split()))
ans = 0
for num in soldier:
    if num > n:
        ans += n
    else:
        ans += num
print(ans)