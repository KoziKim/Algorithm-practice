n = int(input())
a = int(input())

if n%2 == 0:
    print(n//2 + a//2)
else:
    print(n//2 + a//2 + 1)
print(n//2 - a//2)