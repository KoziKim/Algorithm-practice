value = list(map(int, input().split()))

for i in range(6):
    value[i] = value[i] * 5

print(sum(value))