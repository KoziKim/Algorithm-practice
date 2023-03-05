import sys
from itertools import permutations as per
input = sys.stdin.readline

N, k = int(input()), int(input())
cards = [input().rstrip() for i in range(N)]

ans = set()
for p in per(cards,k):
    ans.add(''.join(p))

print(len(ans))