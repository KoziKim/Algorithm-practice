import sys

exp = sys.stdin.readline().split('-')

new_exp = []

for i in exp:
    partial_sum = 0
    num = i.split('+')
    for j in num:
        partial_sum += int(j)
    new_exp.append(partial_sum)

ans = new_exp[0]
for i in range(1, len(new_exp)):
    ans -= new_exp[i]

print(ans)