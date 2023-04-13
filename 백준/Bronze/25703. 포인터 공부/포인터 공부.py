n = int(input())
print('int a;')
print('int *ptr = &a;')
if n >= 2:
    for i in range(n-1):
        if i == 0:
            print('int ', '*'*(i+2), 'ptr', i+2, ' = &ptr;', sep = '')
            continue    
        print('int ', '*'*(i+2), 'ptr', i+2, ' = &ptr', i+1, ';', sep = '')