from collections import deque

h, w = map(int, input().split())

blocks = deque(list(map(int, input().split())))

cnt = 0

# 블록의 아래층부터 한칸씩 위로 올라가면서 물이 고이는 양을 체크할거임
for i in range(h):
    if sum(blocks) == 0: # 0밖에 안들어있으면 탈출하면 됨
        break
    while (blocks[-1] == 0): # 불필요한 우측의 0을 모두 삭제함
        blocks.pop()
    while (blocks[0] == 0): # 불필요한 좌측의 0을 모두 삭제함
        blocks.popleft()
    blen = len(blocks)
    for j in range(blen):
        if blocks[j] == 0: # 물이 고여있다는 뜻이므로 카운트를 늘려줌
            cnt += 1
        if blocks[j] != 0:
            blocks[j] = blocks[j] - 1 # 한층 위를 체크하기 위해 블록을 낮추는 거임

print(cnt)