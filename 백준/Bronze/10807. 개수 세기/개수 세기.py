N = int(input())
nums = list(map(int, input().split()))
v = int(input())
cnt = 0

for i in range(N):
    if v == nums[i]:
        cnt += 1

print(cnt)