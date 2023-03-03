A = []
S = 0
flag = 0

for i in range(9):
    A.append(input())

A = list(map(int, A))

for i in range(9):
    S = S + A[i]

for j in range(9):
    for k in range(j+1, 9):
        if flag == 1:
            break
        if S - (A[j] + A[k]) == 100:
            A[j] = 0
            A[k] = 0
            A.sort()
            for l in range(2, 9):
                print(A[l])
            flag += 1