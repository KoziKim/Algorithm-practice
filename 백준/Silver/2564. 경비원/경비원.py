import sys
garo, sero = map(int, input().split())

store_num = int(input())

stores = []

for i in range(store_num):
    direction, dist_from_end = map(int, sys.stdin.readline().split())
    if direction == 1:
        stores.append(("north", dist_from_end))
    if direction == 2:
        stores.append(("south", dist_from_end))
    if direction == 3:
        stores.append(("west", dist_from_end))
    if direction == 4:
        stores.append(("east", dist_from_end))



dong_pos = list(map(int, input().split()))

if dong_pos[0] == 1:
    d_direction = "north"
if dong_pos[0] == 2:
    d_direction = "south"
if dong_pos[0] == 3:
    d_direction = "west"
if dong_pos[0] == 4:
    d_direction = "east"

d_dist = dong_pos[1]

sum = 0
for i in range(store_num):
    s_direction = stores[i][0]
    s_dist = stores[i][1]
    if s_direction == "north":
        if d_direction == "north":
            sum += abs(s_dist - d_dist)
        if d_direction == "south":
            sum += min(s_dist + d_dist + sero, 2*garo - s_dist - d_dist + sero)
        if d_direction == "west":
            sum += d_dist + s_dist
        if d_direction == "east":
            sum += garo - s_dist + d_dist
    if s_direction == "south":
        if d_direction == "north":
            sum += min(s_dist + d_dist + sero, 2*garo - s_dist - d_dist + sero)
        if d_direction == "south":
            sum += abs(s_dist - d_dist)
        if d_direction == "west":
            sum += sero - d_dist + s_dist
        if d_direction == "east":
            sum += garo - s_dist + sero - d_dist
    if s_direction == "west":
        if d_direction == "north":
            sum += s_dist + d_dist
        if d_direction == "south":
            sum += sero - s_dist + d_dist
        if d_direction == "west":
            sum += abs(s_dist - d_dist)
        if d_direction == "east":
            sum += min(s_dist + d_dist + garo, 2*sero - s_dist - d_dist + garo)
    if s_direction == "east":
        if d_direction == "north":
            sum += garo - d_dist + sero - s_dist
        if d_direction == "south":
            sum += sero - s_dist + garo - d_dist
        if d_direction == "west":
            sum += min(s_dist + d_dist + garo, 2*sero - s_dist - d_dist + garo)
        if d_direction == "east":
            sum += abs(s_dist - d_dist)

print(sum)