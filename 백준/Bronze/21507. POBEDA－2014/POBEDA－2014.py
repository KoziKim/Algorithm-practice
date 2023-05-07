from math import isqrt
a, b, c, d = map(int, input().split())

num_sqrs = min(a, b) + min(c, d)

print(int(isqrt(num_sqrs)))