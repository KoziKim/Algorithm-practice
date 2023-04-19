can = list(map(int, input().split()))

can.sort()

if can[0]**2 + can[1]**2 != can[2]**2 and can[0] == can[1] == can[2]:
    print(2)
elif can[0]**2 + can[1]**2 == can[2]**2 and (can[0] != can[1] or can[1] != can[2] or can[3] != can[1]):
    print(1)
else:
    print(0)
