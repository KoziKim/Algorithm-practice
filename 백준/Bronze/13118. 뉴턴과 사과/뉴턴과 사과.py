people = list(map(int, input().split()))
x, y, r = map(int, input().split())

for i in range(len(people)):
    if x == people[i]:
        print(i+1)
        break
else:
    print(0)