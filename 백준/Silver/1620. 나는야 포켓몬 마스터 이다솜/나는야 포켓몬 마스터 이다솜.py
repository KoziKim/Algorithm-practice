import sys
input = sys.stdin.readline
N, M = map(int, input().split())

pokemon = {}
for i in range(1, N+1):
    a = input().rstrip()
    pokemon[i] = a
    pokemon[a] = i


for i in range(M):
    A = input().rstrip()
    if A.isdigit():
        print(pokemon[int(A)])
    else:
        print(pokemon[A])