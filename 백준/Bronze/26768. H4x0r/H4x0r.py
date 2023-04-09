word = input()
new = []
for i in range(len(word)):
    if word[i] == 'a':
        new.append('4')
    elif word[i] == 'e':
        new.append('3')
    elif word[i] == 'i':
        new.append('1')
    elif word[i] == 'o':
        new.append('0')
    elif word[i] == 's':
        new.append('5')
    else:
        new.append(word[i])
print(*new, sep='')