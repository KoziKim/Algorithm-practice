import sys
input = sys.stdin.readline
T = int(input().rstrip())
for i in range(T):
    A, B = map(int, input().split())
    print(A+B)