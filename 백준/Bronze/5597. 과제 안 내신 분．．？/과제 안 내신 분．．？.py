n = [i for i in range(1, 31)]
N = [int(input()) for j in range(28)]
A=[]
for i in range(30):
    if n[i] not in N:
        A.append(n[i])
A.sort()
print(A[0])
print(A[1])