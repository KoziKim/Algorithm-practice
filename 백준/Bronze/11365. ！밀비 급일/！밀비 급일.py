while True:
    password = input()
    if password == 'END':
        break
    for i in range(len(password)-1, -1, -1):
        print(password[i], end = '')
        if i == 0:
            print()
