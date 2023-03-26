n = int(input())
for _ in range(n):
    word, a, b = input().split()
    for i in range(len(word)):
        if i >= int(a) and i < int(b):
            if i == len(word) - 1:
                print()
            continue
        print(word[i], end ='')
        if i == len(word) - 1:
            print()