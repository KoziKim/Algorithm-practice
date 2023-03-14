import sys

n = int(input())
circles = []
for _ in range(n):
    x, r = map(int, sys.stdin.readline().split())
    circles.append(("L", x - r))
    circles.append(("R", x + r))

circles.sort(key=lambda x: (x[0]),  reverse=True)
circles.sort(key=lambda x: x[1])

stack = []
count = 1

for circle in circles:
    if circle[0] == "L":
        stack.append(circle)
        continue

    total_width = 0
    has_same_width = False

    while stack:
        prev = stack.pop()
        if prev[0] == "L":
            width = circle[1] - prev[1]
            if total_width == width:
                if not has_same_width:
                    count += 2
                    has_same_width = True
            else:
                count += 1
                has_same_width = False
            stack.append(("C", width))
            break
        elif prev[0] == "C":
            total_width += prev[1]

print(count)
