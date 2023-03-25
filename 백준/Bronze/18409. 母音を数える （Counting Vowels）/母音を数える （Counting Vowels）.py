vowel = ["a", "i", "u", "e", "o"]
cnt = 0
n = int(input())
word = input()
for i in range(n):
    if word[i] in vowel:
        cnt += 1
print(cnt)