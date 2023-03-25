import sys
inp = sys.stdin.readline

N = int(inp())

for i in range(N):
    candi = inp().rstrip()
    if 6 <= len(candi) <= 9:
        print("yes")
    else:
        print("no")