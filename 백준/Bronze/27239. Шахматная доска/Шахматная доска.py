from math import ceil
a = int(input())

alpha = ['a','b','c','d','e','f','g','h']

print(alpha[a % 8 - 1], ceil(a/8), sep = '') 