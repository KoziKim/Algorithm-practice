num = input()
car = input().split()
cnt = 0
for i in range(len(car)):
    if num == car[i]:
        cnt+=1
print(cnt)