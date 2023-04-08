n = int(input())
for i in range(n):
    a, b = map(float, input().split())
    print('%.1f'%abs(a-b))