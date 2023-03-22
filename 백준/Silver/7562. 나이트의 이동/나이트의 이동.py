from collections import deque
import sys
input = sys.stdin.readline

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(start_x, start_y, end_x, end_y):

    q = deque()
    q.append([start_x, start_y])
    board[start_x][start_y] = 1

    while q:
        a, b = q.popleft()
        if a == end_x and b == end_y:
            print(board[end_x][end_y] - 1)
            return
        for i in range(8):
            x, y = a + dx[i], b + dy[i]
            if 0 <= x < n and 0 <= y < n and board[x][y] == 0:
                q.append([x, y])
                board[x][y] = board[a][b] + 1

t = int(input())

for i in range(t):
    n = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    bfs(start_x, start_y, end_x, end_y)