four = list(map(int, input().split()))

four.sort()
print(abs(four[0] + four[3] - four[1] - four[2]))