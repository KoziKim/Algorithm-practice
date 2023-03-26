ans = [0] * 26
alph = 'abcdefghijklmnopqrstuvwxyz'
word = input()
for i in range(len(word)):
    for j in range(len(alph)):
        if word[i] == alph[j]:
            ans[j] += 1
print(*ans)