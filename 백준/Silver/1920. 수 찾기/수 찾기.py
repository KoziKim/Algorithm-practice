import sys
input = sys.stdin.readline

N = int(input())
Nnum = set(map(int, input().split()))
M = int(input())
Mnum = list(map(int, input().split()))

for i in range(M):
    if Mnum[i] in Nnum:
        print(1)
    else:
        print(0)