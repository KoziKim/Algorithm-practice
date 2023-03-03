import math

N = input()
num = input().split()
c = []

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for i in range(0, len(num)):
    if num[i] == "1":
        continue
    if is_prime(int(num[i])):
        c.append(num[i])

print(len(c))