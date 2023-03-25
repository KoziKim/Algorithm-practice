ans = []
for i in range(2):
    team = list(map(int, input().split()))
    ans.append(6*team[0]+3*team[1]+2*team[2]+1*team[3]+2*team[4])

print(*ans)