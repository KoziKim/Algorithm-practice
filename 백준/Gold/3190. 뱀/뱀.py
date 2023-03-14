from collections import deque

n = int(input())
k = int(input())
apples = []
for _ in range(k):
    row, col = map(int, input().split())
    apples.append((row-1, col-1))
l = int(input())
turns = []
for _ in range(l):
    x, c = input().split()
    turns.append((int(x), c))

board = [[0] * (n+2) for _ in range(n+2)]  # 테두리를 추가하여 보드 생성
for i in range(n+2):
    board[0][i] = 1  # 가장 윗줄 채우기
    board[n+1][i] = 1  # 가장 아랫줄 채우기
    board[i][0] = 1  # 가장 왼쪽줄 채우기
    board[i][n+1] = 1  # 가장 오른쪽줄 채우기

for row, col in apples:
    board[row+1][col+1] = 2  # 사과 위치 표시

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동, 남, 서, 북
direction = 0  # 초기 방향은 동쪽
snake = deque([(1, 1)])  # 뱀의 초기 위치

time = 0
turn_index = 0
while True:
    time += 1
    row, col = snake[-1]
    dr, dc = directions[direction]
    nr, nc = row + dr, col + dc
    if board[nr][nc] == 1:  # 벽에 부딪힌 경우
        break
    if board[nr][nc] == 0:  # 빈칸인 경우
        tail_row, tail_col = snake.popleft()  # 꼬리를 자름
        board[tail_row][tail_col] = 0  # 꼬리가 있던 자리를 비움
    snake.append((nr, nc))  # 머리를 다음 칸에 위치시킴
    board[nr][nc] = 1  # 머리가 있는 자리를 뱀의 몸통으로 표시

    # 방향 전환
    if turn_index < len(turns) and time == turns[turn_index][0]:
        _, direction_char = turns[turn_index]
        if direction_char == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
        turn_index += 1

print(time)