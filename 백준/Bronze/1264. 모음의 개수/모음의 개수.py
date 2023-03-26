vowel = ['A', 'I', 'E', 'O', 'U', 'a', 'i', 'e', 'o', 'u']
while True:
    cnt = 0
    tcase = input()
    if tcase == '#':
        break
    for i in range(len(tcase)):
        if tcase[i] in vowel:
            cnt += 1
        if i == len(tcase) - 1:
            print(cnt)