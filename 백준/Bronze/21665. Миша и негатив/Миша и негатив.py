n, m = map(int, input().split())
check = []

for i in range(n):
    tmp = input()
    for j in range(len(tmp)):
        if tmp[j] == 'W':
            check.append('B')
        elif tmp[j] == 'B':
            check.append('W')
input()
cnt = 0
for i in range(n):
    tmp = input()
    for j in range(len(tmp)):
        if check[m*i+j] != tmp[j]:
            cnt += 1
print(cnt)