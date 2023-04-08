cost1000, extra = map(int, input().split())
n = int(input())
for i in range(n):
    a = int(input())
    if a > 1000:
        print(a, 1000*cost1000 + extra*(a-1000))
    else:
        print(a, a*cost1000)