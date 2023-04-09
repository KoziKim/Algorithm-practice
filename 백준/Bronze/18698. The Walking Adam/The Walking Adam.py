n = int(input())

for i in range(n):
    a = input()
    cnt = 0
    for j in range(len(a)):
        if a[j] == 'D':
            break
        cnt+=1
    print(cnt)