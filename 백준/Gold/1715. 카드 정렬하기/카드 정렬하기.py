import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
cards = []
for i in range(n):
    heappush(cards, int(input()))

result = 0

if len(cards) == 1:
    print(result)

else:
    for i in range(n-1): # 2개 꺼내고 하나 더하기 떄문에 n-1까지만 탐색
        previous = heappop(cards)
        current = heappop(cards)

        result += previous + current
        heappush(cards, previous + current)
    
    print(result)