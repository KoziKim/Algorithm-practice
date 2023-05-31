# 센서 개수
n = int(input())
# 집중국 개수
k = int(input())
# 센서 좌표
sensors = list(map(int, input().split()))
sensors.sort()
compare = []
if n == 1:
    print(0)
    exit()

for i in range(len(sensors)-1):
    compare.append(sensors[i+1] - sensors[i])

for i in range(k-1):
    a = max(compare)
    compare.remove(a)

print(sum(compare))