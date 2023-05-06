import sys
n, p = map(int, input().split())

stack = [[] for _ in range(7)]

cnt = 0
for i in range(n):
    string_num, fret_num = map(int, sys.stdin.readline().split())
    if not stack[string_num]:
        stack[string_num].append(fret_num)
        cnt += 1
        continue
    if stack[string_num] and stack[string_num][-1] == fret_num:
        continue
    if stack[string_num] and stack[string_num][-1] < fret_num:
        stack[string_num].append(fret_num)
        cnt += 1
    elif stack[string_num] and stack[string_num][-1] > fret_num:
        while stack[string_num] and stack[string_num][-1] > fret_num:
            stack[string_num].pop()
            cnt += 1
        if stack[string_num] and stack[string_num][-1] == fret_num:
            continue
        stack[string_num].append(fret_num)
        cnt+=1

print(cnt)