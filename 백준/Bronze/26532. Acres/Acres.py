a, b = map(int, input().split())
if (a*b)%(5*4840) == 0:
    print((a*b)//(5*4840))
else:
    print((a*b)//(5*4840)+1)