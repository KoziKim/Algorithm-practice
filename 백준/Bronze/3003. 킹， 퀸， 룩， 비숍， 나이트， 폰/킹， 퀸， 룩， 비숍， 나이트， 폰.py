pieces = list(map(int, input().split()))

complete = [1, 1, 2, 2, 2, 8]
plus = [0, 0, 0, 0, 0, 0]

while True:
    if pieces == complete:
        print(*plus)
        break
    for i in range(len(pieces)):
        if pieces[i] == complete[i]:
            continue
        if pieces[i] < complete[i]:
            pieces[i] += 1
            plus[i] += 1
        elif pieces[i] > complete[i]:
            pieces[i] -= 1
            plus[i] -= 1 