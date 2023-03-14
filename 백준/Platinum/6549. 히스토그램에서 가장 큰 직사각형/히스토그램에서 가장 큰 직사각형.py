import sys

input = sys.stdin.readline

res = []
while True:
    h_height = list(map(int, input().split()))
    if h_height[0] == 0:
        break
    stack = []
    n = h_height[0]
    max_area = 0
    for i in range(1, n+1):
        # 스택에 들어간 게 마주친 것보다 크다면,
        # 높이 하나씩 빼가면서 인덱스를 사용해 너비와 곱해서 맥스값 갱신 
        while stack and stack[-1][1] > h_height[i]:
            popped = stack.pop()
            if not stack:
                width = i - 1
            else:
                width = i - stack[-1][0] - 1
            max_area = max(max_area, popped[1] * width)
        stack.append((i, h_height[i]))
    # 검사 후 스택에 뭔가 남아있다면, 나머지 블록에 대해 넓이 계산 진행
    while stack:
        popped = stack.pop()
        if not stack:
            width = n 
        else:
            width = n - stack[-1][0]
        max_area = max(max_area, popped[1] * width)
    print(max_area)