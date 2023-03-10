import sys
bracket = sys.stdin.readline().rstrip()
S = []
ans = 0
tmp = 1

# def listrindex(a, value):
#     return len(a) - a[::-1].index(value) -1

for i in range(len(bracket)):
    if bracket[i] == '(':
        S.append(bracket[i])
        tmp *= 2
    elif bracket[i] == '[':
        S.append(bracket[i])
        tmp *= 3
    elif bracket[i] == ')':
        if '(' in S and S[-1] != '[':
            if bracket[i-1] == '(':
                ans += tmp
            S.pop()
            tmp //= 2
        else:
            ans = 0
            break
    elif bracket[i] == ']':
        if '[' in S and S[-1] != '(':
            if bracket[i-1] == '[':
                ans += tmp
            S.pop()
            tmp //= 3
        else:
            ans = 0
            break
if S:
    print(0)
else:
    print(ans)
