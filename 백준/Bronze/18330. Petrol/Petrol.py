a = int(input())
b = int(input())

if a > 60 + b:
    print(1500*(60+b) + 3000*(a-(60+b)))
else:
    print(1500*a)