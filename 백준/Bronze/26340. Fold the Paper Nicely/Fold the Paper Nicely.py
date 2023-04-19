from math import trunc
n = int(input())

for i in range(n):
    w, l, num = map(int, input().split())
    print(f"Data set: {w} {l} {num}")
    for j in range(num):
        if w >= l:
            w = trunc(w/2)
        elif l >= w:
            l = trunc(l/2)
    if j == num-1:
        print(f"{max(w, l)} {min(w, l)}\n")