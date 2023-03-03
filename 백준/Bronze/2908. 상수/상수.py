A, B = input().split()
C = str()
D = str()

for i in range(0, len(A)):
    C = C + A[len(A)-1-i]
for i in range(0, len(B)):
    D = D + B[len(B)-1-i]

if C > D:
    print(C)
else:
    print(D)