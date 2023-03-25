distance = int(input())
t = 0

while distance > 0:
    distance -= 5
    t += 1
    if distance <= 0:
        break

print(t)