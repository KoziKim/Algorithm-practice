cnt = 0
for i in range(6):
    a = input()
    if a == 'W':
        cnt += 1
if 1 <= cnt <= 2:
    print(3)
elif 3 <= cnt <= 4:
    print(2)
elif 5 <= cnt <= 6:
    print(1)
else:
    print(-1)