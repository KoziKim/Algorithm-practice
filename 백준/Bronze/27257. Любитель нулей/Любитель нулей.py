a = list(input())
cnt = 0
while a[-1] == '0':
    a.pop()
for i in range(len(a)):
    if a[i] == '0':
        cnt += 1
print(cnt)