n = int(input())
nums = list(map(float, input().split()))
num = 0
for i in range(n):
    num += nums[i]**3

print(num**(1/3))