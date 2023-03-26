hamburger = []
bev = []
for i in range(3):
    hamburger.append(int(input()))
for i in range(2):
    bev.append(int(input()))
hamburger.sort()
bev.sort()
print(hamburger[0] + bev[0] - 50)