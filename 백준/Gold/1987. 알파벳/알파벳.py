r, c = map(int, input().split())

board = [list(input()) for _ in range(r)]
ans = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

check = [False for _ in range(26)]

for i in range(r):
    for j in range(c):
        board[i][j] = ord(board[i][j])-65

check = [False for _ in range(26)]

check[board[0][0]] = True

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= r or ny >= c or nx < 0 or ny < 0 or \
            check[board[nx][ny]] == True:
            continue
        check[board[nx][ny]] = True
        dfs(nx, ny, cnt+1)
        check[board[nx][ny]] = False
    return 

dfs(0,0,1)
print(ans)
