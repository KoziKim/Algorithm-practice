import sys
input = sys.stdin.readline

N = int(input())
tower = list(map(int, input().split()))
Stack = []
ans = []

for i in range(N):
    while Stack:
        if Stack[-1][1] > tower[i]:
            ans.append(Stack[-1][0] + 1)
            break
        else:
            Stack.pop()
    if not Stack:
        ans.append(0)
    Stack.append([i, tower[i]])

print(*ans)