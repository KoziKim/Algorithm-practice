y, m, d = map(int,input().split())
ny, nm, nd = map(int,input().split())

if nm > m:
    print(ny-y)
elif nm == m and nd >= d:
    print(ny-y)
else:
    print(ny-y-1)
print(1+(ny-y))
print(ny-y)
