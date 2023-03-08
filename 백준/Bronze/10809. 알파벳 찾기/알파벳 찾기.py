arr = [-1]*26
j = 0
A = input()
alpha = [chr(i) for i in range(97, 123)]

word = []
for i in range(len(A)):
    word.append(A[i])

for i in range(len(word)):
    j = 0
    while alpha[j]:
        if j == 25:
            if alpha[j] == word[i]:
                arr[j] = i
                alpha[j] = "A"
                break
            else:
                break
        if alpha[j] == word[i]:
            arr[j] = i
            alpha[j] = "A"
        j += 1

for i in range(len(arr)):
    if i == len(arr)-1:
        print(arr[i], end ='')
        exit()
    print(arr[i], end=' ')
