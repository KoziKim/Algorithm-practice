al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
check = [0]*26
letter = input()

for i in range(25):
    check[al.index(letter[i])] += 1

print(al[check.index(0)])