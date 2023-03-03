A = []
B = []
N = 1000
tmp = int()

for i in range(0, 9):
    x = input()
    A.append(x)
    B.append(x)

for i in range(0, 8):
    if int(A[i]) > int(A[i+1]):
        tmp = A[i]
        A[i] = A[i+1]
        A[i+1] = tmp
        i = 0

print(A[8])

for i in range(0,9):
    if B[i] == A[8]:
        print(i+1)