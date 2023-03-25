T, S = map(int, input().split())

if S == 1 or not (12 <= T <= 16):
    print(280)
elif (12 <= T <= 16) and S == 0:
    print(320)