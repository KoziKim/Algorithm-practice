import sys
inp = sys.stdin.readline
k = int(inp())

for i in range(k):
    total = 0
    n, s, d = map(int, inp().split()) # n은 배의 수, s는 배의 속도, d는 만기일까지 남은 일수
    for j in range(n):
        di, vi = map(int, inp().split()) # di는 베니스에서 선박 i까지의 거리, vi는 선박 i의 하중 값
        if s*d >= di:
            total += vi
    print(f"Data Set {i+1}:")
    print(f"{total}\n")