n = int(input())

if n != 0:
    nums = list(map(int, input().split()))
    average = sum(nums)/len(nums)
    a = average/average

if n != 0:
    print('%.2f'%a)
else:
    print('divide by zero')