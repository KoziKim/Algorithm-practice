n = int(input())

for i in range(n):
    a, b, c = map(int, input().split())
    print(a, b, c)
    if a < 10 and b < 10 and c < 10:
        print("zilch")
    elif a >= 10 and b >= 10 and c >= 10:
        print("triple-double")
    elif (a >= 10 and b >= 10) or (b >= 10 and c >= 10) or (c >= 10 and a >= 10):
        print("double-double")
    elif a >= 10 or b >= 10 or c >= 10:
        print("double")
    if i != n-1:
        print()