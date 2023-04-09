n = int(input())

def fact(n):
    if n == 0:
        return 1
    ans = n * fact(n-1)
    return ans

if n <= 4:
    print(str(fact(n))[-1])
else:
    print(0)