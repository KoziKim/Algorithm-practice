import sys
inp = sys.stdin.readline
t = int(inp().rstrip())
for i in range(t):
    n = int(inp().rstrip())
    officer = []
    cnt = 0
    lak = []
    for j in range(n):
        officer.append(list(map(int, inp().split())))
    officer.sort()
    # print(officer)
    tmp = officer[0][1]
    for j in range(1, n):
        if officer[j][1] > tmp:
            cnt += 1
        elif officer[j][1] < tmp:
            tmp = officer[j][1]    
    print(n - cnt)
    # print(lak)