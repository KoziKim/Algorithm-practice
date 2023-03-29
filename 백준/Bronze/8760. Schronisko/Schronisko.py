n = int(input())
for i in range(n):
    w, k = map(int, input().split())
    a = w*k
    print(a//2)