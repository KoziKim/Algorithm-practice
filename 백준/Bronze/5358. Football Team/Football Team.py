while True:
    try:
        a = list(input())
        for i in range(len(a)):
            if a[i] == 'i':
                a[i] = 'e'
            elif a[i] == 'e':
                a[i] = 'i'
            elif a[i] == 'I':
                a[i] = 'E'
            elif a[i] == 'E':
                a[i] = 'I'
        print(*a, sep='')
    except:
        exit()