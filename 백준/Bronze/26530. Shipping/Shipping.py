n = int(input())

for i in range(n):
    a = int(input())
    ans = 0
    for j in range(a):
        item = input().split()
        ans += int(item[1])*float(item[2])
    print(f'$%0.2f'%ans)