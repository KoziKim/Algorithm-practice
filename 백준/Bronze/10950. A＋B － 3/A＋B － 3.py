n = int(input())

a = input()
for i in range(1, n):
    a = a + " " + input()

h = a.split()

for j in range (0, n):
    b = int(h[2*j]) + int(h[2*j+1])
    print(b)