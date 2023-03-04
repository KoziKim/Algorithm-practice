import sys
import math

n = 10000
arr = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)+1)):
    if arr[i] == True:
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    a, b = N//2, N//2
    while a > 0:
        if arr[a] and arr[b]:
            print(a, b)
            break
        a -= 1
        b += 1