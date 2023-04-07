n = int(input())

for i in range(n):
    line = input()
    stack = []
    stack.append(line[0])
    for j in range(1, len(line)):
        if line[j] != stack[-1]:
            stack.append(line[j])
    print(*stack, sep='')