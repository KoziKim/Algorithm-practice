a = int(input())
b = int(input())

print(f'All positions change in year {a}')
while a + 60 <= b:
    print(f'All positions change in year {a + 60}')
    a += 60