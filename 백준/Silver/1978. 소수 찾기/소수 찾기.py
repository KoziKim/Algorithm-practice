N = int(input())
datas = list(map(int,input().split()))
temps = [1,3,5,7]
count=0
for data in datas: 
    result = False
    if data ==2:
        count+=1
    for i in range(2,data):
        if data%i == 0:
            result = False
            break
        result = True
    if result:
        count+=1
print(count)