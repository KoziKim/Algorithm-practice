l = int(input())
w = int(input())
h = int(input())

if min(l, w)/h >= 2:
    if l/w <= 2:
        print("good")
        exit()
    elif w/l <= 2:
        print("good")
        exit()
print("bad")