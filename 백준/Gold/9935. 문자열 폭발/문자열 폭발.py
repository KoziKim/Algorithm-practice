a = list(input())
b = list(input())
b_len = len(b)

stack = []
temp = []

for i in range(len(a)):
    stack.append(a[i])
    if stack[-1] == b[-1]:
        cnt = 0
        for j in range(len(b)):
            if stack and stack[-1] == b[-1-j]:
                temp.append(stack.pop())
                cnt += 1
            else:
                break
        if cnt == 0:
            continue
        if cnt == b_len:
            continue
        elif cnt != b_len:
            for k in range(cnt):
                stack.append(temp.pop())
if not stack:
    print("FRULA")
else:
    print(*stack, sep = '')