import sys
N, B = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

def square(X, Y):
    newA = [[0]*N for _ in range(N)]

    for row in range(N):
        for col in range(N):
            sum = 0
            for i in range(N):
                sum += (X[row][i] * Y[i][col])
            newA[row][col] = sum % 1000
    return newA

def recur(A, B):
    if B == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        return A
    
    tmp = recur(A, B // 2)
    if B % 2:
        return square(square(tmp, tmp), A)
    else:
        return square(tmp, tmp)

ans = recur(A, B)

for a in ans:
    print(*a)