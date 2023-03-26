while True:
    line = input().split()
    name = line[0]
    if name == '#':
        break
    age, weight = int(line[1]), int(line[2])
    if age > 17 or weight >= 80:
        print(name, 'Senior')
    else:
        print(name, 'Junior')