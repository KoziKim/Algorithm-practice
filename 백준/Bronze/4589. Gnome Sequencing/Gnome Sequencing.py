n = int(input())
print('Gnomes:')
for i in range(n):
    nums = list(map(int, input().split()))
    if (nums[0] < nums[1] < nums[2]) or (nums[0] > nums[1] > nums[2]) or (nums[0] == nums[1] == nums[2]):
        print('Ordered')
    else:
        print('Unordered')