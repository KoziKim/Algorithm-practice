imo = input()
n = len(imo)
cnt = 0
und = 0
for i in range(6, n-1):
    if imo[i] == '_':
        und += 1
    cnt+=1
print(9+cnt+und*5)