import sys
input = sys.stdin.readline
N = int(input())
cases = [input().rstrip() for i in range(N)]

for case in cases:
    S = []
    for i in case:
        if i == '(':
            S.append('(')
        else:
            if S:
                S.pop()
            else:
                print('NO')
                break
    else:
        if S:
            print('NO')
        else:
            print('YES')