S = input()
T = input()

s_stack = []
t_stack = []

for i in range(len(S)):
    s_stack.append(S[i])
for i in range(len(T)):
    t_stack.append(T[i])

for i in range(len(T)-1, -1, -1):
    if t_stack == s_stack:
        print(1)
        break
    if t_stack[i] == 'A':
        t_stack.pop()
        continue
    if t_stack[i] == 'B':
        t_stack.pop()
        t_stack = t_stack[::-1]
        continue
else:
    print(0)