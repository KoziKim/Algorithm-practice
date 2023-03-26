h, c = map(int, input().split())
loser = (h - c) // 2
if loser < 0 or (h-c)%2 != 0:
    print(-1)
    exit()
winner = h - loser
print(winner, loser)