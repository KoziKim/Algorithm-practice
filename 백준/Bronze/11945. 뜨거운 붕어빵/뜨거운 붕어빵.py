r, c = map(int, input().split())
n_bread = []
for i in range(r):
    new_line = ''
    bread = input()
    for j in range(c-1, -1, -1):
        new_line += bread[j]
    n_bread.append(new_line)
for i in n_bread:
    print(i)