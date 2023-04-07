n = int(input())

for i in range(n):
    a = list(map(int, input().split()))
    if a[0] == 1:
        print(a[0], a[1])
        print(a[1])
    else:
        print(a[0], a[1])
        print(a[1] + ((a[0]-1)*(a[1]-2)))