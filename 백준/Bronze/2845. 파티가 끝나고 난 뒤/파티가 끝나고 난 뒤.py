l, p = map(int, input().split())
nums = list(map(int, input().split()))

compare = l*p
ans = []
for num in nums:
    ans.append(num - compare)
print(*ans)