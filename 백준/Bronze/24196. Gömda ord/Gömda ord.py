word = input()
idx = 0
while idx < len(word) - 1:
    if idx == 0:
        print(word[0], end = '')
    idx += ord(word[idx]) - ord('A') + 1
    if idx > len(word) - 1:
        break
    print(word[idx], end = '')