import sys
input = sys.stdin.readline

V, E = map(int, input().split())
Vroot = [i for i in range(V+1)]
Elist = []
for _ in range(E):
    Elist.append(list(map(int,input().split())))

Elist.sort(key=lambda x: x[2])

def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]

ans = 0
for S, E, W in Elist:
    Sroot = find(S)
    Eroot = find(E)
    if Sroot != Eroot:
        if Sroot > Eroot:
            Vroot[Sroot] = Eroot
        else:
            Vroot[Eroot] = Sroot
        ans += W
 
print(ans)