import sys
input = sys.stdin.readline
N = int(input())
S = []

for i in range(N):
    A = input().split()
    if A[0] == "push":
        S.append(A[1])
    elif A[0] == "top":
        if len(S) <= 0:
            print(-1)
            continue
        print(S[-1])
    elif A[0] == "size":
        print(len(S))
    elif A[0] == "empty":
        if len(S) <= 0:
            print(1)
        else:
            print(0)
    elif A[0] == "pop":
        try:
            num = S.pop()
            print(num)
        except:
            print(-1)