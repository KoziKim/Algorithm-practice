row, col = map(int, input().split())

graph_1 = [list(map(int, input())) for _ in range(row)]
graph_2 = [list(map(int, input())) for _ in range(row)]

cnt = 0

def flip(r, c):
    for i in range(r, r+3):
        for j in range(c, c+3):
            if graph_1[i][j] == 1:
                graph_1[i][j] = 0
            elif graph_1[i][j] == 0:
                graph_1[i][j] = 1

if row >= 3 and col >= 3:
    for r in range(row-2):
        for c in range(col-2):
            if graph_1[r][c] != graph_2[r][c]:
                flip(r, c)
                cnt+=1

if graph_1 != graph_2:
    cnt = -1

print(cnt)