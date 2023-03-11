import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for i in range(N)]
white, blue = 0, 0

def div_conq(x, y, N):
    global white, blue
    tmp_cnt = 0
    for i in range(x, x + N):
        for j in range(y, y + N):
            if paper[i][j]:
                tmp_cnt += 1
    if not tmp_cnt:
        white += 1
    elif tmp_cnt == N**2:
        blue += 1
    else:
        div_conq(x, y, N // 2) # 종이 1 탐색
        div_conq(x, y + N // 2, N // 2) # 종이 2 탐색
        div_conq(x + N // 2, y, N // 2) # 종이 3 탐색
        div_conq(x + N // 2, y + N // 2, N // 2) # 종이 4 탐색
    return

div_conq(0, 0, N)
print(white)
print(blue)