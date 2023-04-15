from collections import deque

h, w = map(int, input().split())

blocks = deque(list(map(int, input().split())))

cnt = 0
for i in range(h):
    if sum(blocks) == 0:
        break
    while (blocks[-1] == 0):
        blocks.pop()
    while (blocks[0] == 0):
        blocks.popleft()
    blen = len(blocks)
    for j in range(blen):
        if blocks[j] == 0:
            cnt += 1
        if blocks[j] != 0:
            blocks[j] = blocks[j] - 1

print(cnt)