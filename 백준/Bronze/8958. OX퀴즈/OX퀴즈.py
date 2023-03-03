N = int(input())
score = 0
k = 1

for i in range(0, N):
    A = input()
    for j in range(0, len(A)):
        if A[j] == "O":
            score = score + k
            if j == len(A) - 1:
                print(score)
                score = 0
                k = 1
            elif A[j+1] == "O":
                k = k + 1
            else:
                k = 1
        elif A[j] == "X":
            k = 1
            if j == len(A) - 1:
                print(score)
                score = 0