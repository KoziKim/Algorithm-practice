A = input()
N = len(A)
ans = 0

for i in range(0, N):
    if N == 1:
        if A[0] == " ":
            print(0)
            break
        else:
            print(1)
            break
    if i == N - 1:
        print(ans + 1)
        break
    if A[0] == " ":
        i = i + 1
    if A[i] == " ":
        if i == N - 1:
            print(ans + 1)
            break
        ans = ans + 1