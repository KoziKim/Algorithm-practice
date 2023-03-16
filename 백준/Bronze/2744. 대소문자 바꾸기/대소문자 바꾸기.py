word = input()

r = ""
for i in word:
    if i.islower():
        r += i.upper()
    elif i.isupper:
        r += i.lower()

print(r)